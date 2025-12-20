"""
Python module for converting Pitão code (Portuguese Python) to standard Python code.
"""

import re
import os


# Portuguese to English keyword mapping
PORTUGUESE_TO_PYTHON = {
    # Boolean and None values
    "Falso": "False",
    "Nulo": "None", 
    "Verdadeiro": "True",
    
    # Logical operators
    "e": "and",
    "ou": "or",
    "nao": "not",
    
    # Control flow
    "se": "if",
    "senaose": "elif",
    "senao": "else",
    "para": "for",
    "enquanto": "while",
    "quebre": "break",
    "continue": "continue",
    "passe": "pass",
    
    # Exception handling
    "tente": "try",
    "exceto": "except",
    "finalmente": "finally",
    "levante": "raise",
    
    # Functions and classes
    "def": "def",
    "classe": "class",
    "retorne": "return",
    "produza": "yield",
    
    # Async
    "assincrono": "async",
    "aguarde": "await",
    
    # Other keywords
    "como": "as",
    "afirme": "assert",
    "del": "del",
    "importe": "import",
    "de": "from",
    "em": "in",
    "eh": "is",
    "com": "with",
    "global": "global",
    "naolocal": "nonlocal",
    "lambda": "lambda",
}

# Reverse mapping for py2pt
PYTHON_TO_PORTUGUESE = {v: k for k, v in PORTUGUESE_TO_PYTHON.items()}


def _is_pitao_file(word):
    """
    Returns True if word ends in .pt or .pit, else False

    Args:
        word (str): Filename to check

    Returns:
        boolean: Whether 'word' ends with '.pt' or '.pit'
    """
    return word.endswith(".pt") or word.endswith(".pit")


def _change_file_name(name, outputname=None, reverse=False):
    """
    Changes *.pt filenames to *.py filenames (or vice versa).

    Args:
        name (str): Filename to edit
        outputname (str): Optional. Overrides result of function.
        reverse (bool): If True, converts .py to .pt

    Returns:
        str: Resulting filename
    """
    if outputname is not None:
        return outputname

    if reverse:
        if name.endswith(".py"):
            return name[:-3] + ".pt"
        return name + ".pt"
    else:
        if name.endswith(".pit"):
            return name[:-4] + ".py"
        if name.endswith(".pt"):
            return name[:-3] + ".py"
        return name + ".py"


def parse_imports(filename):
    """
    Reads the file and scans for imports. Returns all the assumed filenames
    of all the imported modules (ie, module name appended with ".pt" and ".pit")

    Args:
        filename (str): Path to file

    Returns:
        list of str: All imported modules, suffixed with '.pt' and '.pit'
    """
    with open(filename, 'r', encoding='utf-8') as infile:
        infile_str = infile.read()

    # Match both Portuguese "importe" and English "import"
    imports = re.findall(r"(?<=importe\s)[\w.]+(?=;|\s|$)", infile_str)
    imports += re.findall(r"(?<=import\s)[\w.]+(?=;|\s|$)", infile_str)
    imports2 = re.findall(r"(?<=de\s)[\w.]+(?=\s+importe)", infile_str)
    imports2 += re.findall(r"(?<=from\s)[\w.]+(?=\s+import)", infile_str)

    # Return both .pt and .pit suffixes for each import
    all_imports = imports + imports2
    imports_with_suffixes = [im + ".pt" for im in all_imports] + [im + ".pit" for im in all_imports]
    return imports_with_suffixes


def translate_keywords(content, reverse=False):
    """
    Translate keywords between Portuguese and English.
    Skips content inside strings and comments.

    Args:
        content (str): Source code content
        reverse (bool): If True, translate English to Portuguese

    Returns:
        str: Translated source code
    """
    mapping = PYTHON_TO_PORTUGUESE if reverse else PORTUGUESE_TO_PYTHON
    
    # Pattern to match strings and comments
    # This captures: triple-quoted strings, single/double quoted strings, and comments
    string_pattern = r'(\"\"\"[\s\S]*?\"\"\"|\'\'\'[\s\S]*?\'\'\'|\"(?:[^\"\\]|\\.)*\"|\'(?:[^\'\\]|\\.)*\'|#.*$)'
    
    # Split content preserving strings and comments
    parts = re.split(string_pattern, content, flags=re.MULTILINE)
    
    result_parts = []
    for i, part in enumerate(parts):
        # Odd indices are the matched strings/comments, don't translate them
        if i % 2 == 1:
            result_parts.append(part)
        else:
            # Translate keywords in code
            translated_part = part
            for source, target in mapping.items():
                pattern = r'\b' + re.escape(source) + r'\b'
                translated_part = re.sub(pattern, target, translated_part)
            result_parts.append(translated_part)
    
    return ''.join(result_parts)


def parse_file(filepath, filename_prefix="", outputname=None, change_imports=None):
    """
    Converts a Pitão file to a Python file and writes it to disk.

    Args:
        filepath (str): Path to the Pitão file you want to parse.
        filename_prefix (str): Prefix to resulting file name.
        outputname (str): Optional. Override name of output file.
        change_imports (dict): Names of imported Pitão modules and their
            Python alternative.
    """
    filename = os.path.basename(filepath)
    filedir = os.path.dirname(filepath)

    output_path = os.path.join(filedir, filename_prefix + _change_file_name(filename, outputname))
    
    with open(filepath, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Translate Portuguese keywords to English
    translated = translate_keywords(content, reverse=False)

    # Change imported names if necessary
    if change_imports is not None:
        for module in change_imports:
            translated = re.sub(
                r"(?<=import\s){}".format(module),
                "{} as {}".format(change_imports[module], module),
                translated
            )
            translated = re.sub(
                r"(?<=from\s){}(?=\s+import)".format(module),
                change_imports[module],
                translated
            )

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(translated)

    return output_path


def reverse_parse_file(filepath, filename_prefix="", outputname=None):
    """
    Converts a Python file to a Pitão file and writes it to disk.

    Args:
        filepath (str): Path to the Python file you want to parse.
        filename_prefix (str): Prefix to resulting file name.
        outputname (str): Optional. Override name of output file.
    """
    filename = os.path.basename(filepath)
    filedir = os.path.dirname(filepath)

    output_path = os.path.join(
        filedir, 
        filename_prefix + _change_file_name(filename, outputname, reverse=True)
    )
    
    with open(filepath, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Translate English keywords to Portuguese
    translated = translate_keywords(content, reverse=True)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(translated)

    return output_path
