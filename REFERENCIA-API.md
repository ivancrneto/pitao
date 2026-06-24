# Referência Completa da API

> Referência de todas as traduções disponíveis em Pytão.

## CLI (Linha de Comando)

### pitao

Executa arquivos Pytão.

```bash
pitao [opções] arquivo.pt [args...]

Opções:
  -c          Compila para .py sem executar
  -k          Mantém o arquivo .py gerado
  -v          Modo verbose (mostra tradução)
  --help      Mostra esta ajuda
```

**Exemplos:**
```bash
pitao ola_mundo.pt
pitao -c script.pt
pitao -k arquivo.pt
```

### pt2py

Traduz arquivos Pytão para Python.

```bash
pt2py [opções] arquivo.pt

Opções:
  -o ARQUIVO    Define nome do arquivo de saída
```

**Exemplos:**
```bash
pt2py script.pt
pt2py -o output.py script.pt
```

### py2pt

Traduz arquivos Python para Pytão.

```bash
py2pt [opções] arquivo.py

Opções:
  -o ARQUIVO    Define nome do arquivo de saída
```

**Exemplos:**
```bash
py2pt script.py
py2pt -o output.pt script.py
```

---

## Palavras Reservadas

### Valores Booleanos

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `Verdadeiro` | `True` | Valor booleano verdadeiro |
| `Falso` | `False` | Valor booleano falso |
| `Nulo` | `None` | Valor nulo |

### Operadores Lógicos

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `e` | `and` | E lógico |
| `ou` | `or` | OU lógico |
| `nao` | `not` | Negação |

### Controle de Fluxo

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `se` | `if` | Condicional |
| `senaose` | `elif` | Condicional else-if |
| `senao` | `else` | Condicional else |
| `para` | `for` | Loop for |
| `enquanto` | `while` | Loop while |
| `quebre` | `break` | Interrompe loop |
| `continue` | `continue` | Próxima iteração |
| `passe` | `pass` | Placeholder |

### Funções e Classes

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `def` | `def` | Define função |
| `classe` | `class` | Define classe |
| `retorne` | `return` | Retorna valor |
| `produza` | `yield` | Produz valor |
| `lambda` | `lambda` | Função anônima |

### Exceções

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `tente` | `try` | Bloco try |
| `exceto` | `except` | Bloco except |
| `finalmente` | `finally` | Bloco finally |
| `levante` | `raise` | Levanta exceção |
| `afirme` | `assert` | Assertiva |

### Async

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `assincrono` | `async` | Define função async |
| `aguarde` | `await` | Aguarda async |

### Imports

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `importe` | `import` | Importa módulo |
| `de` | `from` | Importa de módulo |
| `como` | `as` | Alias |

### Outros

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `em` | `in` | Pertence a |
| `eh` | `is` | É idéntico a |
| `usando` | `with` | Context manager (`com` é alias legado) |
| `del` | `del` | Deleta |
| `global` | `global` | Variável global |
| `naolocal` | `nonlocal` | Variável nonlocal |

---

## Funções Built-in

### I/O

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `imprimir(*args)` | `print(*args)` | Imprime |
| `entrada(texto)` | `input(texto)` | Lê entrada |
| `abrir(arquivo, modo)` | `open(arquivo, modo)` | Abre arquivo |

### Tipo

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `inteiro(x)` | `int(x)` | Converte para int |
| `flutuante(x)` | `float(x)` | Converte para float |
| `texto(x)` | `str(x)` | Converte para string |
| `booleano(x)` | `bool(x)` | Converte para bool |
| `lista(x)` | `list(x)` | Converte para list |
| `dicionario(x)` | `dict(x)` | Converte para dict |
| `conjunto(x)` | `set(x)` | Converte para set |
| `tupla(x)` | `tuple(x)` | Converte para tuple |

### Sequência

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `tamanho(seq)` | `len(seq)` | Tamanho |
| `intervalo(inicio, fim, passo)` | `range(inicio, fim, passo)` | Range |
| `enumerar(seq)` | `enumerate(seq)` | Enumera |
| `juntar(*seqs)` | `zip(*seqs)` | Zip |
| `ordenado(seq)` | `sorted(seq)` | Ordenado |
| `invertido(seq)` | `reversed(seq)` | Invertido |
| `soma(seq)` | `sum(seq)` | Soma |
| `max(*args)` | `max(*args)` | Máximo |
| `min(*args)` | `min(*args)` | Mínimo |

### Iteração

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `mapear(func, seq)` | `map(func, seq)` | Mapeia |
| `filtrar(func, seq)` | `filter(func, seq)` | Filtra |
| `todos(seq)` | `all(seq)` | Todos verdadeiros |
| `algum(seq)` | `any(seq)` | Algum verdadeiro |

### Inspeção

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `tipo(x)` | `type(x)` | Tipo |
| `ehinstancia(x, tipo)` | `isinstance(x, tipo)` | É instância |
| `ehsubclasse(x, tipo)` | `issubclass(x, tipo)` | É subclasse |
| `tematributo(obj, nome)` | `hasattr(obj, nome)` | Tem atributo |
| `obteratributo(obj, nome)` | `getattr(obj, nome)` | Obtém atributo |
| `defatributo(obj, nome, valor)` | `setattr(obj, nome, valor)` | Define atributo |
| `delatributo(obj, nome)` | `delattr(obj, nome)` | Deleta atributo |
| `diretorio(obj)` | `dir(obj)` | Lista atributos |
| `variaveis(obj)` | `vars(obj)` | Dict de atributos |
| `identificador(obj)` | `id(obj)` | ID do objeto |
| `chamavel(obj)` | `callable(obj)` | É chamável |

### Matemática

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `absoluto(x)` | `abs(x)` | Valor absoluto |
| `arredondar(x, n)` | `round(x, n)` | Arredonda |
| `potencia(base, exp)` | `pow(base, exp)` | Potência |

### Representação

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `representacao(obj)` | `repr(obj)` | Representação |
| `formatar(obj, fmt)` | `format(obj, fmt)` | Formata |
| `binario(x)` | `bin(x)` | Binário |
| `hexadecimal(x)` | `hex(x)` | Hexadecimal |
| `octal(x)` | `oct(x)` | Octal |
| `caractere(x)` | `chr(x)` | Caractere |
| `codigo(c)` | `ord(c)` | Código |

### Iteradores

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `iterador(obj)` | `iter(obj)` | Iterador |
| `proximo(it)` | `next(it)` | Próximo |

### Avançadas

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `avaliar(expr)` | `eval(expr)` | Eval |
| `executar(code)` | `exec(code)` | Exec |
| `compilar(code, modo)` | `compile(code, modo)` | Compila |
| `globais()` | `globals()` | Globais |
| `locais()` | `locals()` | Locais |

### OOP

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `metodoclasse(func)` | `classmethod(func)` | Método de classe |
| `metodoestatico(func)` | `staticmethod(func)` | Método estático |
| `propriedade(func)` | `property(func)` | Propriedade |
| `objeto()` | `object()` | Objeto base |

### Memória

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `vetor_bytes(dados)` | `bytearray(dados)` | Bytearray |
| `visao_memoria(obj)` | `memoryview(obj)` | Memoryview |
| `conjunto_congelado(seq)` | `frozenset(seq)` | Frozenset |

### Utilitários

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `hash(obj)` | `hash(obj)` | Hash |
| `ajuda(obj)` | `help(obj)` | Ajuda |

---

## Métodos de Objeto

### String (texto)

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `texto.maiuscula()` | `str.upper()` | Maiúsculas |
| `texto.minuscula()` | `str.lower()` | Minúsculas |
| `texto.capitalizar()` | `str.capitalize()` | Capitaliza |
| `texto.titulo()` | `str.title()` | Título |
| `texto.removerespacos()` | `str.strip()` | Remove espaços |
| `texto.dividir_(sep)` | `str.split(sep)` | Divide |
| `texto.substituir(old, new)` | `str.replace(old, new)` | Substitui |
| `texto.encontrar(sub)` | `str.find(sub)` | Encontra |
| `texto.comecacom(prefix)` | `str.startswith(prefix)` | Começa com |
| `texto.terminacom(suffix)` | `str.endswith(suffix)` | Termina com |
| `texto.ehdigito()` | `str.isdigit()` | É dígito |
| `texto.ehalfa()` | `str.isalpha()` | É letra |
| `texto.ehalfanum()` | `str.isalnum()` | É alfanumérico |

### List (lista)

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `lista.adicionar_(item)` | `list.append(item)` | Adiciona |
| `lista.estender(items)` | `list.extend(items)` | Estende |
| `lista.inserir(i, item)` | `list.insert(i, item)` | Insere |
| `lista.remover(item)` | `list.remove(item)` | Remove |
| `lista.retirar()` | `list.pop()` | Retira |
| `lista.limpar()` | `list.clear()` | Limpa |
| `lista.indice(item)` | `list.index(item)` | Índice |
| `lista.contar(item)` | `list.count(item)` | Conta |
| `lista.ordenar()` | `list.sort()` | Ordena |
| `lista.inverter()` | `list.reverse()` | Inverte |
| `lista.copiar()` | `list.copy()` | Copia |

### Dict (dicionario)

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `dicionario.chaves()` | `dict.keys()` | Chaves |
| `dicionario.valores()` | `dict.values()` | Valores |
| `dicionario.itens()` | `dict.items()` | Itens |
| `dicionario.obter(chave)` | `dict.get(chave)` | Obtém |
| `dicionario.atualizar(d)` | `dict.update(d)` | Atualiza |
| `dicionario.definirpadrao(chave, valor)` | `dict.setdefault(chave, valor)` | Define padrão |

---

## Exceções

| Pytão | Python |
|-------|--------|
| `Excecao` | `Exception` |
| `ErroValor` | `ValueError` |
| `ErroTipo` | `TypeError` |
| `ErroChave` | `KeyError` |
| `ErroIndice` | `IndexError` |
| `ErroAtributo` | `AttributeError` |
| `ErroNome` | `NameError` |
| `ErroArquivoNaoEncontrado` | `FileNotFoundError` |
| `ErroDivisaoPorZero` | `ZeroDivisionError` |
| `ErroImportacao` | `ImportError` |
| `ErroExecucao` | `RuntimeError` |
| `NaoImplementado` | `NotImplementedError` |
| `PararIteracao` | `StopIteration` |
| `InterrupcaoTeclado` | `KeyboardInterrupt` |

---

## Biblioteca Padrão

### os

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `listardir(caminho)` | `os.listdir(caminho)` | Lista diretório |
| `criardir(caminho)` | `os.mkdir(caminho)` | Cria diretório |
| `removedir(caminho)` | `os.rmdir(caminho)` | Remove diretório |
| `existir(caminho)` | `os.path.exists(caminho)` | Existe |
| `caminhounir(*parts)` | `os.path.join(*parts)` | Junta caminhos |

### sys

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `argumentos` | `sys.argv` | Argumentos |
| `caminho` | `sys.path` | Path |
| `sair(codigo)` | `sys.exit(codigo)` | Sai |

### datetime

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `agora()` | `datetime.now()` | Agora |
| `hoje()` | `datetime.today()` | Hoje |
| `data()` | `date` | Date |
| `hora()` | `time` | Time |

### math

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `raizquadrada(x)` | `math.sqrt(x)` | Raiz quadrada |
| `pi` | `math.pi` | Pi |
| `teto(x)` | `math.ceil(x)` | Teto |
| `piso(x)` | `math.floor(x)` | Piso |

### random

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `aleatorio()` | `random.random()` | Aleatório |
| `escolher(seq)` | `random.choice(seq)` | Escolhe |
| `intaleatorio(a, b)` | `random.randint(a, b)` | Int aleatório |

### json

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `carregartexto(s)` | `json.loads(s)` | Carrega texto |
| `despejartexto(obj)` | `json.dumps(obj)` | Despeja texto |
| `carregar(f)` | `json.load(f)` | Carrega |
| `despejar(obj, f)` | `json.dump(obj, f)` | Despeja |

### re

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `combinar(pattern, string)` | `re.match(pattern, string)` | Match |
| `buscar(pattern, string)` | `re.search(pattern, string)` | Search |
| `encontrartodos(pattern, string)` | `re.findall(pattern, string)` | Find all |
| `sub(pattern, repl, string)` | `re.sub(pattern, repl, string)` | Sub |

---

## Módulos Especiais

### caminho (os.path)

| Pytão | Python | Descrição |
|-------|--------|-----------|
| `caminho.existe(p)` | `os.path.exists(p)` | Existe |
| `caminho.ehdir(p)` | `os.path.isdir(p)` | É diretório |
| `caminho.eharq(p)` | `os.path.isfile(p)` | É arquivo |