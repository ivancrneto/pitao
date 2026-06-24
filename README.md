# Pitão 🐍

<p align="center">
  <img src="https://raw.githubusercontent.com/ivancrneto/pitao/main/pitao.jpg" alt="Pitão Logo" width="200"/>
</p>

**Pitão é um pré-processador que traduz código Portuguese → Python.**

> ⚠️ **Importante:** Pitão **não é** Python. É uma ferramenta de tradução. O código Python "real" é sempre em inglês. Nosso objetivo é ajudar falantes de português a aprender e escrever Python mais facilmente.

## O que é Pitão?

Pitão permite escrever código usando palavras reservadas em português, que são automaticamente traduzidas para Python antes da execução.

**Pitão é Python - apenas com palavras em português.**

### Por que existe?

- **Aprendizagem:** Reduz a barreira linguística para iniciantes
- **Prototipagem:** Escreva lógica rapidamente em português
- **Educação:** Ensine programação com material didático em português

### O que NÃO é

- ❌ Uma linguagem de programação diferente
- ❌ Um substituto para Python
- ❌ Uma tentativa de "portugalizar" Python

**Código Pitão é traduzido para Python real.** Você pode converter qualquer arquivo `.pt` para `.py` e obter Python padrão.

---

## Instalação

```bash
pip install pitao
```

Ou para instalar localmente com `uv`:

```bash
git clone https://github.com/ivancrneto/pitao.git
cd pitao
uv sync
```

---

## Galeria

![Sintaxe Básica](https://raw.githubusercontent.com/ivancrneto/pitao/main/vscode-pitao/assets/pitao1.png)
![Controle de Fluxo](https://raw.githubusercontent.com/ivancrneto/pitao/main/vscode-pitao/assets/pitao2.png)

---

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
pitao ola_mundo.pt
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
- `pitao` → `python` (pitão para Python)
- `pt2py` → Traduz .pt para .py
- `py2pt` → Traduz .py para .pt

### 🛠️ Ferramentas
- **CLI completa** com modo verbose
- **Compilação** sem execução (`-c`)
- **Manutenção** do arquivo gerado (`-k`)

## Perguntas Frequentes

**Pitão é Python?**
> Tecnicamente não. É um pré-processador que traduz código português para Python. O resultado final é sempre Python real.

**Posso usar bibliotecas Python?**
> Sim! Bibliotecas são importadas normalmente. O código Python de bibliotecas permanece em inglês.

**Pitão é para iniciantes?**
> Principalmente. É uma ferramenta de aprendizagem. Python "real" sempre usará palavras em inglês.

**Devo usar Pitão em produção?**
> Não recomendamos. Python padrão é a linguagem - Pitão é apenas uma ferramenta de tradução.

## Documentação

- [README](README.md) - Visão geral
- [ROADMAP.md](ROADMAP.md) - Plano de desenvolvimento
- [GUIA-MIGRACAO.md](GUIA-MIGRACAO.md) - Guia de migração Python ↔ Pitão
- [REFERENCIA-API.md](REFERENCIA-API.md) - Referência completa da API
- [EXEMPLOS.md](EXEMPLOS.md) - Exemplos práticos
- [FAQ.md](FAQ.md) - Perguntas frequentes

## Palavras Reservadas

| Português    | Python     |
| ------------ | ---------- |
| `Falso`      | `False`    |
| `Verdadeiro` | `True`     |
| `Nulo`       | `None`     |
| `e`          | `and`      |
| `ou`         | `or`       |
| `nao`        | `not`      |
| `se`         | `if`       |
| `senaose`    | `elif`     |
| `senao`      | `else`     |
| `para`       | `for`      |
| `enquanto`   | `while`    |
| `quebre`     | `break`    |
| `continue`   | `continue` |
| `def`        | `def`      |
| `classe`     | `class`    |
| `retorne`    | `return`   |
| `produza`    | `yield`    |
| `tente`      | `try`      |
| `exceto`     | `except`   |
| `finalmente` | `finally`  |
| `levante`    | `raise`    |
| `assincrono` | `async`    |
| `aguarde`    | `await`    |
| `importe`    | `import`   |
| `de`         | `from`     |
| `como`       | `as`       |
| `em`         | `in`       |
| `eh`         | `is`       |
| `usando`     | `with`     |
| `afirme`     | `assert`   |
| `del`        | `del`      |
| `global`     | `global`   |
| `naolocal`   | `nonlocal` |
| `lambda`     | `lambda`   |
| `passe`      | `pass`     |

---

## Funções Built-in

Pitão também suporta a tradução de algumas funções built-in do Python:

| Português      | Python        |
| -------------- | ------------- |
| `imprimir()`   | `print()`     |
| `entrada()`    | `input()`     |
| `abrir()`      | `open()`      |
| `inteiro()`    | `int()`       |
| `flutuante()`  | `float()`     |
| `texto()`      | `str()`       |
| `booleano()`   | `bool()`      |
| `lista()`      | `list()`      |
| `dicionario()` | `dict()`      |
| `conjunto()`   | `set()`       |
| `tupla()`      | `tuple()`     |
| `tamanho()`    | `len()`       |
| `intervalo()`  | `range()`     |
| `enumerar()`   | `enumerate()` |
| `juntar()`     | `zip()`       |
| `ordenar()`    | `sorted()`    |
| `inverter()`   | `reversed()`  |
| `somar()`      | `sum()`       |
| `maior_de()`   | `max()`       |
| `menor_de()`   | `min()`       |

---

## Comandos

### `pitao` - Executar arquivos Pitão

```bash
pitao arquivo.pt [args...]     # Executa o arquivo
pitao -c arquivo.pt            # Compila para .py sem executar
pitao -k arquivo.pt           # Executa e mantém o .py gerado
pitao -v arquivo.pt           # Modo verbose
```

### `pt2py` - Traduzir Pitão para Python

```bash
pt2py arquivo.pt               # Cria arquivo.py
pt2py -o saida.py arquivo.pt  # Especifica nome de saída
```

### `py2pt` - Traduzir Python para Pitão

```bash
py2pt arquivo.py               # Cria arquivo.pt
py2pt -o saida.pt arquivo.py  # Especifica nome de saída
```

---

## Licença

MIT

---

<p align="center">
Feito com ❤️ para a comunidade de programação brasileira
</p>