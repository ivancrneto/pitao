from pitao.parser import translate_keywords


def test_sequence():
    code = "tamanho([1,2,3]) + intervalo(10) + enumerar([1,2])"
    result = translate_keywords(code)
    assert result == "len([1,2,3]) + range(10) + enumerate([1,2])"


def test_sequence2():
    code = "ordenar([3,1,2]) + inverter([1,2,3]) + somar([1,2,3])"
    result = translate_keywords(code)
    assert result == "sorted([3,1,2]) + reversed([1,2,3]) + sum([1,2,3])"


def test_sequence_min_max():
    code = "maior_de([1,2,3]) + menor_de([1,2,3])"
    result = translate_keywords(code)
    assert result == "max([1,2,3]) + min([1,2,3])"


def test_iteration():
    code = "mapear(int, ['1','2']) + filtrar(lambda x: x > 0, [-1, 0, 1])"
    result = translate_keywords(code)
    assert result == "map(int, ['1','2']) + filter(lambda x: x > 0, [-1, 0, 1])"


def test_iteration2():
    code = "todos([True, True]) + algum([False, True])"
    result = translate_keywords(code)
    assert result == "all([True, True]) + any([False, True])"
