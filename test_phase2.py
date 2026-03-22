from pitao.parser import translate_keywords


def test_sequence():
    code = "tamanho([1,2,3]) + intervalo(10) + enumerar([1,2])"
    result = translate_keywords(code)
    assert "len" in result
    assert "range" in result
    assert "enumerate" in result


def test_sequence2():
    code = "ordenado([3,1,2]) + invertido([1,2,3]) + soma([1,2,3])"
    result = translate_keywords(code)
    assert "sorted" in result
    assert "reversed" in result
    assert "sum" in result


def test_iteration():
    code = "mapear(int, ['1','2']) + filtrar(lambda x: x > 0, [-1, 0, 1])"
    result = translate_keywords(code)
    assert "map" in result
    assert "filter" in result


def test_iteration2():
    code = "todos([True, True]) + algum([False, True])"
    result = translate_keywords(code)
    assert "all" in result
    assert "any" in result
