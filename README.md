# Pitão 🐍

<p align="center">
  <img src="https://raw.githubusercontent.com/ivancrneto/pitao/main/pitao.jpg" alt="Pitão Logo" width="200"/>
</p>

**Pytão é um pré-processador que traduz código Portuguese → Python.**

> ⚠️ **Importante:** Pitão **não é** Python. É uma ferramenta de tradução. O código Python "real" é sempre em inglês. Nosso objetivo é ajudar falantes de português a aprender e escrever Python mais facilmente.

## O que é Pitão?

Pytão permite escrever código usando palavras reservadas em português, que são automaticamente traduzidas para Python antes da execução.

**Pytão é Python - apenas com palavras em português.**

### Por que existe?

- **Aprendizagem:** Reduz a barreira linguística para iniciantes
- **Prototipagem:** Escreva lógica rapidamente em português
- **Educação:** Ensine programação com material didático em português

### O que NÃO é

- ❌ Uma linguagem de programação diferente
- ❌ Um substituto para Python
- ❌ Uma tentativa de "portugalizar" Python

**Código Pytão é traduzido para Python real.** Você pode converter qualquer arquivo `.pt` para `.py` e obter Python padrão.

## Instalação

```bash
pip install pytão
```

Ou para instalar localmente com `uv`:

```bash
git clone https://github.com/ivancrneto/pytão.git
cd pytão
uv sync
```

## Início Rápido

Crie um arquivo `ola_mundo.pt`:

```python
# ola_mundo.pt
def ola_mundo():
    imprimir("Olá, Mundo!")

se __nome__ == "__principal__":
    ola_mundo()
```

Execute com:

```bash
pytão ola_mundo.pt
# Saída: Olá, Mundo!
```

O código é traduzido para:

```python
# ola_mundo.py (gerado automaticamente)
def ola_mundo():
    print("Olá, Mundo!")

if __name__ == "__main__":
    ola_mundo()
```

## Características

### ✨ Tradução Completa
- 53+ palavras-chave traduzidas
- 70+ funções built-in
- 30+ métodos de objetos (string, list, dict)
- 15+ tipos de exceção
- 25+ funções da biblioteca padrão
- Suporte a métodos encadeados

### 🔄 Bidirecional
- `pytão` → `python` (pytão para Python)
- `pt2py` → Traduz .pt para .py
- `py2pt` → Traduz .py para .pt

### 🛠️ Ferramentas
- **CLI completa** com modo verbose
- **Compilação** sem execução (`-c`)
- **Manutenção** do arquivo gerado (`-k`)

## Perguntas Frequentes

**Pytão é Python?**
> Tecnicamente não. É um pré-processador que traduz código português para Python. O resultado final é sempre Python real.

**Posso usar bibliotecas Python?**
> Sim! Bibliotecas são importadas normalmente. O código Python de bibliotecas permanece em inglês.

**Pytão é para iniciantes?**
> Principalmente. É uma ferramenta de aprendizagem. Python "real" sempre usará palavras em inglês.

**Devo usar Pytão em produção?**
> Não recomendamos. Python padrão é a linguagem - Pytão é apenas uma ferramenta de tradução.

## Documentação

- [README](README.md) - Visão geral
- [ROADMAP.md](ROADMAP.md) - Plano de desenvolvimento
- [GUIA-MIGRACAO.md](GUIA-MIGRACAO.md) - Guia de migração Python ↔ Pytão
- [REFERENCIA-API.md](REFERENCIA-API.md) - Referência completa da API
- [EXEMPLOS.md](EXEMPLOS.md) - Exemplos práticos
- [FAQ.md](FAQ.md) - Perguntas frequentes

## Palavras Reservadas

| Português | Python | | Português | Python |
|-----------|--------|---|-----------|--------|
| `Falso` | `False` | | `importe` | `import` |
| `Nulo` | `None` | | `em` | `in` |
| `Verdadeiro` | `True` | | `eh` | `is` |
| `e` | `and` | | `nao` | `not` |
| `ou` | `or` | | `passe` | `pass` |
| `se` | `if` | | `retorne` | `return` |
| `senaose` | `elif` | | `tente` | `try` |
| `senao` | `else` | | `exceto` | `except` |
| `para` | `for` | | `finalmente` | `finally` |
| `enquanto` | `while` | | `levante` | `raise` |
| `quebre` | `break` | | `com` | `with` |
| `continue` | `continue` | | `produza` | `yield` |
| `def` | `def` | | `assincrono` | `async` |
| `classe` | `class` | | `aguarde` | `await` |
| `del` | `del` | | `afirme` | `assert` |
| `de` | `from` | | `como` | `as` |
| `global` | `global` | | `naolocal` | `nonlocal` |

## Comandos

### `pytão` - Executar arquivos Pytão

```bash
pytão arquivo.pt [args...]     # Executa o arquivo
pytão -c arquivo.pt            # Compila para .py sem executar
pytão -k arquivo.pt           # Executa e mantém o .py gerado
pytão -v arquivo.pt           # Modo verbose
```

### `pt2py` - Traduzir Pytão para Python

```bash
pt2py arquivo.pt               # Cria arquivo.py
pt2py -o saida.py arquivo.pt  # Especifica nome de saída
```

### `py2pt` - Traduzir Python para Pytão

```bash
py2pt arquivo.py               # Cria arquivo.pt
py2pt -o saida.pt arquivo.py  # Especifica nome de saída
```

## Licença

MIT

---

<p align="center">
Feito com ❤️ para a comunidade de programação brasileira
</p>