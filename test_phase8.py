from pitao.parser import translate_keywords


def test_os_functions():
    code = "listardir('.') + criardir('novo_dir') + removedir('dir')"
    result = translate_keywords(code)
    assert "listdir" in result
    assert "mkdir" in result
    assert "rmdir" in result


def test_sys_variables():
    code = "argumentos + caminho"
    result = translate_keywords(code)
    assert "argv" in result
    assert "path" in result


def test_datetime():
    code = "agora() + hoje() + data() + hora()"
    result = translate_keywords(code)
    assert "now" in result
    assert "today" in result
    assert "date" in result
    assert "time" in result


def test_math_functions():
    code = "raizquadrada(16) + teto(3.7) + piso(3.7)"
    result = translate_keywords(code)
    assert "sqrt" in result
    assert "ceil" in result
    assert "floor" in result


def test_math_constant():
    code = "x = pi"
    result = translate_keywords(code)
    assert "pi" in result


def test_random_functions():
    code = "aleatorio() + escolher([1,2,3]) + intaleatorio(1, 10)"
    result = translate_keywords(code)
    assert "random" in result
    assert "choice" in result
    assert "randint" in result


def test_json_functions():
    code = 'carregartexto("{}") + despejartexto({"a":1})'
    result = translate_keywords(code)
    assert "loads" in result
    assert "dumps" in result


def test_re_functions():
    code = 'combinar("a", "abc") + buscar("b", "abc") + encontrartodos("a", "abc")'
    result = translate_keywords(code)
    assert "match" in result
    assert "search" in result
    assert "findall" in result


def test_path_methods():
    code = 'caminho.existe("arquivo") + caminho.ehdir("dir") + caminho.eharq("file")'
    result = translate_keywords(code)
    assert "path.exists" in result
    assert "path.isdir" in result
    assert "path.isfile" in result
