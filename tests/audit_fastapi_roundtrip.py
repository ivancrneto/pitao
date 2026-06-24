"""
Scale round-trip audit of the Pitão translator against a real third-party
framework (FastAPI, and optionally its dependencies).

For every ``.py`` file in the installed FastAPI source tree this script computes
the round trip ``py -> pt -> py`` (``translate_keywords`` applied in reverse and
then forward) and reports where the original source is NOT recovered. Each
corrupted token is classified so we can separate defects that are *fixable* by
the translator from those that are *inherent* to a regex translator with no
scope analysis.

It runs the round trip in two modes:

  * ``before`` - the pre-fix behaviour (keyword pass with a plain ``\\b`` word
    boundary, path predicates treated as keywords), and
  * ``after``  - the current behaviour (keyword pass with a ``(?<!\\.)``
    lookbehind, path predicates moved to the dotted method pass).

so the impact of the attribute-corruption fix is visible as a before/after
table.

Usage::

    python tests/audit_fastapi_roundtrip.py            # print summary to stdout
    python tests/audit_fastapi_roundtrip.py --write    # also (re)write the report
    python tests/audit_fastapi_roundtrip.py --packages fastapi starlette pydantic

The Markdown report is written to ``testcases/FASTAPI_AUDIT.md`` (committed).
Intermediate translated files are never written to disk; everything is in
memory.
"""

import argparse
import importlib
import os
import re
import sys

# Make the package importable when run directly from the repo root.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pitao.parser import (  # noqa: E402
    PORTUGUESE_TO_PYTHON,
    PYTHON_TO_PORTUGUESE,
    PORTUGUESE_METHODS,
    PYTHON_TO_PORTUGUESE_METHODS,
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_PATH = os.path.join(REPO_ROOT, "testcases", "FASTAPI_AUDIT.md")

# Path predicates that the fix moved from the keyword map to the method map.
PATH_PREDICATES = {"existe": "exists", "ehdir": "isdir", "eharq": "isfile"}

# English builtins/identifiers that double as Python keyword-map *targets*, used
# to bucket reverse-direction corruption (e.g. an identifier named ``type``).
BUILTIN_IDENTIFIERS = {
    "type", "id", "format", "hash", "next", "iter", "object", "property",
    "path", "now", "today", "date", "time", "round", "sum", "min", "max",
    "map", "filter", "input", "open", "dir", "vars", "copy", "index", "count",
}
DATETIME_SHORTWORDS = {"data", "date", "hora", "time"}

STRING_PATTERN = (
    r"(\"\"\"[\s\S]*?\"\"\"|\'\'\'[\s\S]*?\'\'\'|"
    r"\"(?:[^\"\\]|\\.)*\"|\'(?:[^\'\\]|\\.)*\'|#.*$)"
)
DUNDER_MAPPINGS = {"__nome__": "__name__", "__principal__": "__main__"}
DUNDER_MAPPINGS_REVERSE = {v: k for k, v in DUNDER_MAPPINGS.items()}


def _maps(fixed):
    """Return (keyword_map, method_map) for each direction in the given mode."""
    if fixed:
        return (
            PORTUGUESE_TO_PYTHON,
            PYTHON_TO_PORTUGUESE,
            PORTUGUESE_METHODS,
            PYTHON_TO_PORTUGUESE_METHODS,
        )
    # Pre-fix: path predicates lived in the keyword map, not the method map.
    pt2py_kw = dict(PORTUGUESE_TO_PYTHON)
    pt2py_kw.update(PATH_PREDICATES)
    py2pt_kw = {v: k for k, v in pt2py_kw.items()}
    pt_methods = {
        k: v for k, v in PORTUGUESE_METHODS.items() if k not in PATH_PREDICATES
    }
    py_methods = {v: k for k, v in pt_methods.items()}
    return pt2py_kw, py2pt_kw, pt_methods, py_methods


def _translate(content, reverse, fixed):
    """A parameterised clone of parser.translate_keywords.

    ``fixed`` toggles the ``(?<!\\.)`` lookbehind on the keyword pass (and the
    path-predicate categorisation), so we can reproduce both the pre-fix and
    post-fix behaviour from a single code path.
    """
    pt2py_kw, py2pt_kw, pt_methods, py_methods = _maps(fixed)
    mapping = py2pt_kw if reverse else pt2py_kw
    method_mapping = py_methods if reverse else pt_methods
    dunder_map = DUNDER_MAPPINGS_REVERSE if reverse else DUNDER_MAPPINGS
    prefix = r"(?<!\.)\b" if fixed else r"\b"

    parts = re.split(STRING_PATTERN, content, flags=re.MULTILINE)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            translated = part
            if not part.startswith("#"):
                for source, target in dunder_map.items():
                    translated = translated.replace(source, target)
            out.append(translated)
        else:
            translated = part
            for source, target in method_mapping.items():
                translated = re.sub(
                    r"\." + re.escape(source) + r"\b", "." + target, translated
                )
            for source, target in mapping.items():
                translated = re.sub(
                    prefix + re.escape(source) + r"\b", target, translated
                )
            out.append(translated)
    return "".join(out)


def _round_trip(source, fixed):
    """py -> pt -> py."""
    return _translate(_translate(source, reverse=True, fixed=fixed),
                      reverse=False, fixed=fixed)


# Token regex: words (identifiers) so we can diff token-by-token with the
# character that precedes each token (to detect attribute access).
TOKEN_RE = re.compile(r"\w+")


def _classify(orig_line, rt_line):
    """Yield (bucket, original_token, roundtripped_token) for each corruption."""
    orig_tokens = list(TOKEN_RE.finditer(orig_line))
    rt_tokens = list(TOKEN_RE.finditer(rt_line))
    if len(orig_tokens) != len(rt_tokens):
        # Token count changed (rare); we cannot align reliably.
        yield ("other", orig_line.strip(), rt_line.strip())
        return
    for om, rm in zip(orig_tokens, rt_tokens):
        a, b = om.group(), rm.group()
        if a == b:
            continue
        start = om.start()
        preceded_by_dot = start > 0 and orig_line[start - 1] == "."
        if preceded_by_dot:
            yield ("attribute_corruption", a, b)
        elif len(a) == 1:
            yield ("single_letter_id", a, b)
        elif a in DATETIME_SHORTWORDS:
            yield ("datetime_shortword", a, b)
        elif a in BUILTIN_IDENTIFIERS:
            yield ("builtin_as_identifier", a, b)
        else:
            yield ("other", a, b)


def _audit_source(source, fixed):
    """Return dict: bucket -> list of (orig_token, rt_token) and corrupted-line count."""
    rt = _round_trip(source, fixed)
    if rt == source:
        return {}, 0
    buckets = {}
    corrupted_lines = 0
    for orig_line, rt_line in zip(source.splitlines(), rt.splitlines()):
        if orig_line == rt_line:
            continue
        corrupted_lines += 1
        for bucket, a, b in _classify(orig_line, rt_line):
            buckets.setdefault(bucket, []).append((a, b))
    return buckets, corrupted_lines


def _iter_py_files(package_names):
    files = []
    for name in package_names:
        try:
            module = importlib.import_module(name)
        except ImportError:
            print(f"  [skip] package not installed: {name}", file=sys.stderr)
            continue
        root = os.path.dirname(os.path.abspath(module.__file__))
        for dirpath, _dirs, filenames in os.walk(root):
            for filename in filenames:
                if filename.endswith(".py"):
                    files.append(os.path.join(dirpath, filename))
    return sorted(files)


def run_audit(package_names):
    files = _iter_py_files(package_names)
    versions = {}
    for name in package_names:
        try:
            versions[name] = importlib.import_module(name).__version__
        except Exception:
            versions[name] = "?"

    results = {}
    for mode in ("before", "after"):
        fixed = mode == "after"
        files_touched = 0
        line_count = 0
        bucket_lines = {}
        bucket_examples = {}
        for path in files:
            try:
                with open(path, "r", encoding="utf-8") as handle:
                    source = handle.read()
            except (OSError, UnicodeDecodeError):
                continue
            buckets, corrupted_lines = _audit_source(source, fixed)
            if buckets:
                files_touched += 1
                line_count += corrupted_lines
                for bucket, pairs in buckets.items():
                    bucket_lines[bucket] = bucket_lines.get(bucket, 0) + len(pairs)
                    ex = bucket_examples.setdefault(bucket, [])
                    for a, b in pairs:
                        snippet = f"{a} -> {b}"
                        if snippet not in ex and len(ex) < 4:
                            ex.append(snippet)
        results[mode] = {
            "files_touched": files_touched,
            "total_files": len(files),
            "corrupted_lines": line_count,
            "bucket_lines": bucket_lines,
            "bucket_examples": bucket_examples,
        }
    return results, versions, len(files)


def _format_report(results, versions, total_files):
    lines = []
    lines.append("# FastAPI Round-Trip Audit")
    lines.append("")
    lines.append(
        "Automatically generated by `tests/audit_fastapi_roundtrip.py`. "
        "Do not edit by hand; regenerate with `--write`."
    )
    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    lines.append(
        "For every `.py` file in the installed framework source we compute the "
        "round trip `py -> pt -> py` (`translate_keywords` reverse then forward) "
        "and count lines that are not recovered byte-for-byte. Each corrupted "
        "token is bucketed by *why* it broke."
    )
    lines.append("")
    versions_str = ", ".join(f"`{k}` {v}" for k, v in versions.items())
    lines.append(f"- Packages audited: {versions_str}")
    lines.append(f"- Python `.py` files scanned: **{total_files}**")
    lines.append("")
    lines.append("## Before / after the attribute-corruption fix")
    lines.append("")
    lines.append(
        "`before` = keyword pass with a plain `\\b` boundary (pre-fix). "
        "`after` = keyword pass with a `(?<!\\.)` lookbehind plus the path "
        "predicates moved to the dotted method pass (current code)."
    )
    lines.append("")
    lines.append("| Metric | before | after |")
    lines.append("| --- | ---: | ---: |")
    b, a = results["before"], results["after"]
    lines.append(
        f"| Files corrupted (of {total_files}) | {b['files_touched']} | {a['files_touched']} |"
    )
    lines.append(
        f"| Corrupted lines | {b['corrupted_lines']} | {a['corrupted_lines']} |"
    )
    all_buckets = sorted(set(b["bucket_lines"]) | set(a["bucket_lines"]))
    for bucket in all_buckets:
        lines.append(
            f"| &nbsp;&nbsp;{bucket} | "
            f"{b['bucket_lines'].get(bucket, 0)} | {a['bucket_lines'].get(bucket, 0)} |"
        )
    lines.append("")
    lines.append("## Corruption classes (after the fix)")
    lines.append("")
    if not a["bucket_lines"]:
        lines.append("_No corruption remains._")
    for bucket in all_buckets:
        count_after = a["bucket_lines"].get(bucket, 0)
        examples = a["bucket_examples"].get(bucket) or b["bucket_examples"].get(bucket, [])
        ex_str = ", ".join(f"`{e}`" for e in examples) if examples else "-"
        lines.append(f"- **{bucket}** - {count_after} line(s) after fix. Examples: {ex_str}")
    lines.append("")
    lines.append("## Fixable vs. inherent")
    lines.append("")
    lines.append(
        "- **Fixed (regex-feasible):** `attribute_corruption` - a `(?<!\\.)` "
        "lookbehind on the keyword pass stops `obj.data` becoming `obj.date` "
        "and `x.type` becoming `x.tipo`. Path predicates "
        "(`existe`/`ehdir`/`eharq`) were miscategorised as keywords and were "
        "moved into the dotted method pass, where they round-trip correctly."
    )
    lines.append(
        "- **By design:** the FastAPI fluent API `.get` maps to `.obter`, so "
        "`@app.get` round-trips through the Portuguese spelling. Pitão authors "
        "write `@app.obter`; this is lossless within Pitão's model."
    )
    lines.append(
        "- **Inherent (NOT regex-fixable without scope analysis):** "
        "`single_letter_id` such as `e -> and` (this turns `except ... as e:` "
        "into `except ... as and:`, a `SyntaxError` - the highest-severity "
        "class), `datetime_shortword` such as `data -> date`, and "
        "`builtin_as_identifier` such as a variable named `type`/`id`. A bare "
        "identifier is indistinguishable from a keyword by regex alone; the "
        "only true fix is an AST/scope-aware translation pass. Mitigation today "
        "is authoring discipline in `.pt` files (see `testcases/fastapi_app.pt`)."
    )
    lines.append("")
    return "\n".join(lines)


def _print_summary(results, versions, total_files):
    b, a = results["before"], results["after"]
    print(f"Scanned {total_files} .py files: " + ", ".join(
        f"{k} {v}" for k, v in versions.items()))
    print(f"  before fix: {b['files_touched']} files / {b['corrupted_lines']} lines corrupted")
    print(f"  after  fix: {a['files_touched']} files / {a['corrupted_lines']} lines corrupted")
    print("  per-bucket (before -> after):")
    for bucket in sorted(set(b["bucket_lines"]) | set(a["bucket_lines"])):
        print(f"    {bucket}: {b['bucket_lines'].get(bucket, 0)} -> "
              f"{a['bucket_lines'].get(bucket, 0)}")
    if a["bucket_lines"].get("attribute_corruption", 0) != 0:
        print("  WARNING: attribute_corruption is non-zero after the fix!", file=sys.stderr)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--packages", nargs="+", default=["fastapi"],
        help="packages to audit (default: fastapi)",
    )
    parser.add_argument(
        "--write", action="store_true",
        help="write the Markdown report to testcases/FASTAPI_AUDIT.md",
    )
    args = parser.parse_args(argv)

    results, versions, total_files = run_audit(args.packages)
    if total_files == 0:
        print("No source files found; is FastAPI installed?", file=sys.stderr)
        return 1
    _print_summary(results, versions, total_files)
    if args.write:
        report = _format_report(results, versions, total_files)
        with open(REPORT_PATH, "w", encoding="utf-8") as handle:
            handle.write(report + "\n")
        print(f"Wrote report to {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
