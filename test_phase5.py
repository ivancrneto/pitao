from pitao.parser import translate_keywords


def test_dunder_creation():
    code = "def __iniciar__(self): pass\ndef __texto__(self): return ''"
    result = translate_keywords(code)
    assert "__init__" in result
    assert "__str__" in result


def test_dunder_arithmetic():
    code = "__adic__ + __sub__ + __mul__ + __div__"
    result = translate_keywords(code)
    assert "__add__" in result
    assert "__sub__" in result
    assert "__mul__" in result
    assert "__truediv__" in result


def test_dunder_comparison():
    code = "__igual__ + __menor__ + __maior__"
    result = translate_keywords(code)
    assert "__eq__" in result
    assert "__lt__" in result
    assert "__gt__" in result


def test_dunder_access():
    code = "__obteritem__ + __defitem__ + __delitem__"
    result = translate_keywords(code)
    assert "__getitem__" in result
    assert "__setitem__" in result
    assert "__delitem__" in result


def test_dunder_iteration():
    code = "__iterador__ + __proximo__"
    result = translate_keywords(code)
    assert "__iter__" in result
    assert "__next__" in result


def test_dunder_context():
    code = "__entrar__ + __sair__ + __chamar__"
    result = translate_keywords(code)
    assert "__enter__" in result
    assert "__exit__" in result
    assert "__call__" in result


def test_dunder_special():
    code = "__nome__ + __principal__ + __arquivo__ + __repr__ + __tamanho__"
    result = translate_keywords(code)
    assert "__name__" in result
    assert "__main__" in result
    assert "__file__" in result
    assert "__repr__" in result
    assert "__len__" in result
