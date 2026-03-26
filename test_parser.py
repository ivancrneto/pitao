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