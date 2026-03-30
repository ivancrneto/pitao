from pitao.parser import translate_keywords

# Reorganizing code structure; giving credit to the original contributor for their part.

# ----- Tests, developed by developerfred   ----->>>
def test_io():
    assert "print" in translate_keywords('imprimir("x")')
    assert "input" in translate_keywords('entrada("x")')
    assert "open" in translate_keywords('abrir("x")')


def test_type_conversion():
    code = "inteiro(1) + flutuante(2) + texto(3) + booleano(1)"
    result = translate_keywords(code)
    assert "int" in result
    assert "float" in result
    assert "str" in result
    assert "bool" in result


def test_type_constructors():
    code = "lista([1]) + dicionario({}) + conjunto([1]) + tupla([1])"
    result = translate_keywords(code)
    assert "list" in result
    assert "dict" in result
    assert "set" in result
    assert "tuple" in result


# ----- Tests, developed by IsraelBonicenha ----->>>
def test_booleans_and_none():
    code = "Falso + Nulo + Verdadeiro"
    result = translate_keywords(code)
    assert "False" in result
    assert "None" in result
    assert "True" in result


def test_logical_operators():
    code = "e + ou + nao"
    result = translate_keywords(code)
    assert "and" in result
    assert "or" in result
    assert "not" in result


def test_control_flow():
    code = "se senaose senao para enquanto quebre continue passe"
    result = translate_keywords(code)
    assert "if " in result
    assert "elif" in result
    assert "else" in result
    assert "for" in result
    assert "while" in result
    assert "break" in result
    assert "continue" in result
    assert "pass" in result


def test_exceptions():
    code = "tente exceto finalmente levante"
    result = translate_keywords(code)
    assert "try" in result
    assert "except" in result
    assert "finally" in result
    assert "raise" in result


def test_functions_and_classes():
    code = "def classe retorne produza"
    result = translate_keywords(code)
    assert "def" in result
    assert "class" in result
    assert "return" in result
    assert "yield" in result


def test_async_keywords():
    code = "assincrono aguarde"
    result = translate_keywords(code)
    assert "async" in result
    assert "await" in result


def test_sequence_functions():
    code = "tamanho([1,2,3]) + intervalo(5) + enumerar([1]) + juntar([1],[2]) + ordenar([3,1]) + inverter([1,2]) + somar([1,2]) + maior_de(1,2,3) + menor_de(1,2,3)"
    result = translate_keywords(code)
    assert "len" in result
    assert "range" in result
    assert "enumerate" in result
    assert "zip" in result
    assert "sorted" in result
    assert "reversed" in result
    assert "sum" in result
    assert "max" in result
    assert "min" in result


def test_other_keywords():
    code = "como afirme del importe de em eh com global naolocal lambda"
    result = translate_keywords(code)
    assert "as" in result
    assert "assert" in result
    assert "del" in result
    assert "import" in result
    assert "from" in result
    assert "in" in result
    assert "is" in result
    assert "with" in result
    assert "global" in result
    assert "nonlocal" in result
    assert "lambda" in result


def test_dunder_name_identifier():
    """__nome__ as an identifier (outside strings) translates to __name__."""
    result = translate_keywords("__nome__")
    assert "__name__" in result
    assert "__nome__" not in result


def test_dunder_main_identifier():
    """__principal__ as an identifier translates to __main__."""
    result = translate_keywords("__principal__")
    assert "__main__" in result
    assert "__principal__" not in result


def test_dunder_main_guard_full():
    """The full idiomatic guard pattern translates correctly (identifier + string literal)."""
    code = 'se __nome__ == "__principal__":'
    result = translate_keywords(code)
    assert result == 'if __name__ == "__main__":'


def test_dunder_reverse_full():
    """Reverse translation: the full guard converts from Python back to Pitão."""
    code = 'if __name__ == "__main__":'
    result = translate_keywords(code, reverse=True)
    assert result == 'se __nome__ == "__principal__":'


def test_dunder_comment_untouched():
    """Dunder tokens inside comments are NOT translated."""
    code = "# use __nome__ to check __principal__"
    result = translate_keywords(code)
    # Comments are preserved as-is
    assert "__name__" not in result
    assert "__main__" not in result