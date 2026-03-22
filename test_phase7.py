from pitao.parser import translate_keywords


def test_string_methods():
    code = 'texto("Ola").maiuscula() + texto("Ola").minuscula() + texto("ola").capitalizar()'
    result = translate_keywords(code)
    assert ".upper()" in result
    assert ".lower()" in result
    assert ".capitalize()" in result


def test_string_methods2():
    code = 'texto("Ola Mundo").titulo() + texto("  ola  ").removerespacos()'
    result = translate_keywords(code)
    assert ".title()" in result
    assert ".strip()" in result


def test_string_methods3():
    code = 'texto("a,b,c").dividir(",") + texto("a:b").substituir(":", "-")'
    result = translate_keywords(code)
    assert ".split(" in result
    assert ".replace(" in result


def test_string_methods4():
    code = 'texto("hello").encontrar("lo") + texto("hello").comecacom("he") + texto("hello").terminacom("lo")'
    result = translate_keywords(code)
    assert ".find(" in result
    assert ".startswith(" in result
    assert ".endswith(" in result


def test_string_methods5():
    code = (
        'texto("123").ehdigito() + texto("abc").ehalfa() + texto("abc123").ehalfanum()'
    )
    result = translate_keywords(code)
    assert ".isdigit()" in result
    assert ".isalpha()" in result
    assert ".isalnum()" in result


def test_list_methods():
    code = "lista([1,2,3]).adicionar(4) + lista([1,2]).estender([3,4])"
    result = translate_keywords(code)
    assert ".append(" in result
    assert ".extend(" in result


def test_list_methods2():
    code = "lista([1,2,3]).inserir(0, 0) + lista([1,2,3]).remover(2)"
    result = translate_keywords(code)
    assert ".insert(" in result
    assert ".remove(" in result


def test_list_methods3():
    code = "lista([1,2,3]).retirar() + lista([1,2,3]).indice(2)"
    result = translate_keywords(code)
    assert ".pop(" in result
    assert ".index(" in result


def test_list_methods4():
    code = (
        "lista([1,2,3]).contar(1) + lista([3,1,2]).ordenar() + lista([1,2]).inverter()"
    )
    result = translate_keywords(code)
    assert ".count(" in result
    assert ".sort(" in result
    assert ".reverse(" in result


def test_dict_methods():
    code = 'dicionario({"a":1}).chaves() + dicionario({"a":1}).valores()'
    result = translate_keywords(code)
    assert ".keys()" in result
    assert ".values()" in result


def test_dict_methods2():
    code = 'dicionario({"a":1}).itens() + dicionario({"a":1}).obter("a")'
    result = translate_keywords(code)
    assert ".items()" in result
    assert ".get(" in result


def test_dict_methods3():
    code = (
        'dicionario({"a":1}).atualizar({"b":2}) + dicionario({}).definirpadrao("x", 1)'
    )
    result = translate_keywords(code)
    assert ".update(" in result
    assert ".setdefault(" in result
