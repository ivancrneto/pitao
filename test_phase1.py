from pitao.parser import translate_keywords


def test_io():
    assert translate_keywords('imprimir("x")') == 'print("x")'
    assert translate_keywords('entrada("x")') == 'input("x")'
    assert translate_keywords('abrir("x")') == 'open("x")'


def test_type_conversion():
    code = "inteiro(1) + flutuante(2) + texto(3) + booleano(1)"
    result = translate_keywords(code)
    assert result == "int(1) + float(2) + str(3) + bool(1)"


def test_type_constructors():
    code = "lista([1]) + dicionario({}) + conjunto([1]) + tupla([1])"
    result = translate_keywords(code)
    assert result == "list([1]) + dict({}) + set([1]) + tuple([1])"
