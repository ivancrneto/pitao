from pitao.parser import translate_keywords


def test_advanced():
    code = 'avaliar("1+1") + executar("x = 1") + compilar("x", "exec")'
    result = translate_keywords(code)
    assert "eval" in result
    assert "exec" in result
    assert "compile" in result


def test_advanced2():
    code = "globais() + locais() + chamavel(lambda x: x)"
    result = translate_keywords(code)
    assert "globals" in result
    assert "locals" in result
    assert "callable" in result


def test_oop():
    code = "metodoclasse(func) + metodoestatico(func) + propriedade(func)"
    result = translate_keywords(code)
    assert "classmethod" in result
    assert "staticmethod" in result
    assert "property" in result


def test_bytes():
    code = "vetor_bytes([1,2,3]) + visao_memoria(b'123') + conjunto_congelado([1,2,3])"
    result = translate_keywords(code)
    assert "bytearray" in result
    assert "memoryview" in result
    assert "frozenset" in result


def test_utils():
    code = "hash(x) + ajuda(x)"
    result = translate_keywords(code)
    assert "hash" in result
    assert "help" in result
