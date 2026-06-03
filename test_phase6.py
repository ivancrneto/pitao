from pitao.parser import translate_keywords


def test_exceptions():
    code = "levante Excecao()\nlevante ErroValor('msg')\nlevante ErroTipo('msg')"
    result = translate_keywords(code)
    assert "Exception" in result
    assert "ValueError" in result
    assert "TypeError" in result


def test_exceptions2():
    code = "ErroChave('x') + ErroIndice(0) + ErroAtributo('x')"
    result = translate_keywords(code)
    assert "KeyError" in result
    assert "IndexError" in result
    assert "AttributeError" in result


def test_exceptions3():
    code = "ErroNome('x') + ErroArquivoNaoEncontrado('x') + ErroDivisaoPorZero()"
    result = translate_keywords(code)
    assert "NameError" in result
    assert "FileNotFoundError" in result
    assert "ZeroDivisionError" in result


def test_exceptions4():
    code = "ErroImportacao() + ErroExecucao() + NaoImplementado()"
    result = translate_keywords(code)
    assert "ImportError" in result
    assert "RuntimeError" in result
    assert "NotImplementedError" in result


def test_exceptions5():
    code = "PararIteracao() + InterrupcaoTeclado()"
    result = translate_keywords(code)
    assert "StopIteration" in result
    assert "KeyboardInterrupt" in result
