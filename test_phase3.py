from pitao.parser import translate_keywords


def test_inspection():
    code = "tipo(x) + ehinstancia(x, int) + tematributo(x, 'foo')"
    result = translate_keywords(code)
    assert "type" in result
    assert "isinstance" in result
    assert "hasattr" in result


def test_inspection2():
    code = "obteratributo(x, 'name') + defatributo(x, 'name', 'foo')"
    result = translate_keywords(code)
    assert "getattr" in result
    assert "setattr" in result


def test_math():
    code = "absoluto(-5) + arredondar(3.7) + potencia(2, 3)"
    result = translate_keywords(code)
    assert "abs" in result
    assert "round" in result
    assert "pow" in result


def test_representation():
    code = "representacao(x) + formatar(3.14, '.2f') + binario(10) + hexadecimal(255)"
    result = translate_keywords(code)
    assert "repr" in result
    assert "format" in result
    assert "bin" in result
    assert "hex" in result


def test_representation2():
    code = "octal(8) + caractere(65) + codigo('A')"
    result = translate_keywords(code)
    assert "oct" in result
    assert "chr" in result
    assert "ord" in result


def test_iterators():
    code = "iterador(x) + proximo(i)"
    result = translate_keywords(code)
    assert "iter" in result
    assert "next" in result
