from pitao.parser import translate_keywords


def test_io_functions():
    code = 'imprimir("Olá")\nentrada("Digite: ")\nabrir("arquivo.txt")'
    result = translate_keywords(code)
    assert "print" in result
    assert "input" in result
    assert "open" in result


def test_type_conversion():
    code = 'inteiro("5")\nflutuante("3.14")\ntexto(123)\nbooleano(1)\nlista((1,2,3))\ndicionario({"a": 1})\nconjunto([1,2,2,3])\ntupla([1,2,3])'
    result = translate_keywords(code)
    assert "int(" in result
    assert "float(" in result
    assert "str(" in result
    assert "bool(" in result
    assert "list(" in result
    assert "dict(" in result
    assert "set(" in result
    assert "tuple(" in result


def test_sequence_functions():
    code = "tamanho([1,2,3])\nintervalo(10)\nenumerar([1,2,3])\njuntar([1,2], [3,4])\nordenado([3,1,2])\ninvertido([1,2,3])\nsoma([1,2,3])"
    result = translate_keywords(code)
    assert "len(" in result
    assert "range(" in result
    assert "enumerate(" in result
    assert "zip(" in result
    assert "sorted(" in result
    assert "reversed(" in result
    assert "sum(" in result


def test_iteration_functions():
    code = 'mapear(int, ["1","2","3"])\nfiltrar(lambda x: x > 0, [-1, 0, 1])\ntodos([True, True, False])\nalgum([False, False, True])'
    result = translate_keywords(code)
    assert "map(" in result
    assert "filter(" in result
    assert "all(" in result
    assert "any(" in result


def test_string_methods():
    code = 'texto("Ola").maiuscula()\ntexto("OLA").minuscula()\ntexto("hello").capitalizar()'
    result = translate_keywords(code)
    assert "str(" in result
    assert ".upper()" in result
    assert ".lower()" in result
    assert ".capitalize()" in result


def test_list_methods():
    code = "lista([1,2,3]).adicionar(4)\nlista([1,2,3]).remover(2)\nlista([3,1,2]).ordenar()"
    result = translate_keywords(code)
    assert "list(" in result
    assert ".append(" in result
    assert ".remove(" in result
    assert ".sort(" in result


def test_dict_methods():
    code = 'dicionario({"a":1}).chaves()\ndicionario({"a":1}).valores()\ndicionario({"a":1}).obter("a")'
    result = translate_keywords(code)
    assert "dict(" in result
    assert ".keys()" in result
    assert ".values()" in result
    assert ".get(" in result


def test_all_keywords_translate():
    all_keywords = [
        "Falso",
        "Nulo",
        "Verdadeiro",
        "e",
        "ou",
        "nao",
        "se",
        "senaose",
        "senao",
        "para",
        "enquanto",
        "quebre",
        "continue",
        "passe",
        "tente",
        "exceto",
        "finalmente",
        "levante",
        "def",
        "classe",
        "retorne",
        "produza",
        "assincrono",
        "aguarde",
        "imprimir",
        "entrada",
        "abrir",
        "inteiro",
        "flutuante",
        "texto",
        "booleano",
        "lista",
        "dicionario",
        "conjunto",
        "tupla",
        "tamanho",
        "intervalo",
        "enumerar",
        "juntar",
        "ordenado",
        "invertido",
        "soma",
        "mapear",
        "filtrar",
        "todos",
        "algum",
        "tipo",
        "ehinstancia",
        "ehsubclasse",
        "tematributo",
        "obteratributo",
        "defatributo",
        "delatributo",
        "diretorio",
        "variaveis",
        "identificador",
        "absoluto",
        "arredondar",
        "potencia",
        "representacao",
        "formatar",
        "binario",
        "hexadecimal",
        "octal",
        "caractere",
        "codigo",
        "iterador",
        "proximo",
        "avaliar",
        "executar",
        "compilar",
        "globais",
        "locais",
        "chamavel",
        "metodoclasse",
        "metodoestatico",
        "propriedade",
        "objeto",
        "vetor_bytes",
        "visao_memoria",
        "conjunto_congelado",
        "hash",
        "ajuda",
        "Excecao",
        "ErroValor",
        "ErroTipo",
        "ErroChave",
        "ErroIndice",
        "ErroAtributo",
        "ErroNome",
        "ErroArquivoNaoEncontrado",
        "ErroDivisaoPorZero",
        "ErroImportacao",
        "ErroExecucao",
        "NaoImplementado",
        "PararIteracao",
        "InterrupcaoTeclado",
    ]
    for kw in all_keywords:
        code = f"x = {kw}"
        result = translate_keywords(code)
        assert kw not in result or result != code, f"Failed to translate {kw}"
