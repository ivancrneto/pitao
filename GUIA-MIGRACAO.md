# Guia de Migração: Python ↔ Pytão

> Este guia mostra como migrar código entre Python e Pytão.

## Tradução Automática

Use os comandos integrados para converter código:

```bash
# Python → Pytão
py2pt arquivo.py -o arquivo.pt

# Pytão → Python  
pt2py arquivo.pt -o arquivo.py
```

## Referência Rápida

### Palavras-Chave

| Python | Pytão | Categoria |
|--------|-------|-----------|
| `True` | `Verdadeiro` |布尔 |
| `False` | `Falso` | 布尔 |
| `None` | `Nulo` | 布尔 |
| `and` | `e` | 逻辑 |
| `or` | `ou` | 逻辑 |
| `not` | `nao` | 逻辑 |
| `if` | `se` | 控制流 |
| `elif` | `senaose` | 控制流 |
| `else` | `senao` | 控制流 |
| `for` | `para` | 循环 |
| `while` | `enquanto` | 循环 |
| `break` | `quebre` | 循环 |
| `continue` | `continue` | 循环 |
| `def` | `def` | 函数 |
| `return` | `retorne` | 函数 |
| `yield` | `produza` | 函数 |
| `class` | `classe` | OOP |
| `try` | `tente` | 异常 |
| `except` | `exceto` | 异常 |
| `finally` | `finalmente` | 异常 |
| `raise` | `levante` | 异常 |
| `import` | `importe` | 导入 |
| `from` | `de` | 导入 |
| `as` | `como` | 导入 |
| `with` | `com` | 上下文 |
| `async` | `assincrono` | 异步 |
| `await` | `aguarde` | 异步 |

### Funções Built-in

| Python | Pytão |
|--------|-------|
| `print()` | `imprimir()` |
| `input()` | `entrada()` |
| `open()` | `abrir()` |
| `int()` | `inteiro()` |
| `float()` | `flutuante()` |
| `str()` | `texto()` |
| `bool()` | `booleano()` |
| `list()` | `lista()` |
| `dict()` | `dicionario()` |
| `set()` | `conjunto()` |
| `tuple()` | `tupla()` |
| `len()` | `tamanho()` |
| `range()` | `intervalo()` |
| `enumerate()` | `enumerar()` |
| `zip()` | `juntar()` |
| `sorted()` | `ordenado()` |
| `reversed()` | `invertido()` |
| `sum()` | `soma()` |
| `map()` | `mapear()` |
| `filter()` | `filtrar()` |
| `all()` | `todos()` |
| `any()` | `algum()` |
| `type()` | `tipo()` |
| `isinstance()` | `ehinstancia()` |
| `abs()` | `absoluto()` |
| `round()` | `arredondar()` |
| `pow()` | `potencia()` |
| `repr()` | `representacao()` |
| `format()` | `formatar()` |
| `bin()` | `binario()` |
| `hex()` | `hexadecimal()` |
| `oct()` | `octal()` |
| `chr()` | `caractere()` |
| `ord()` | `codigo()` |
| `iter()` | `iterador()` |
| `next()` | `proximo()` |
| `eval()` | `avaliar()` |
| `exec()` | `executar()` |
| `compile()` | `compilar()` |
| `globals()` | `globais()` |
| `locals()` | `locais()` |
| `callable()` | `chamavel()` |
| `hasattr()` | `tematributo()` |
| `getattr()` | `obteratributo()` |
| `setattr()` | `defatributo()` |
| `delattr()` | `delatributo()` |
| `dir()` | `diretorio()` |
| `vars()` | `variaveis()` |
| `id()` | `identificador()` |
| `hash()` | `hash()` |
| `help()` | `ajuda()` |
| `classmethod` | `metodoclasse()` |
| `staticmethod` | `metodoestatico()` |
| `property` | `propriedade()` |
| `object` | `objeto()` |
| `bytearray` | `vetor_bytes()` |
| `memoryview` | `visao_memoria()` |
| `frozenset` | `conjunto_congelado()` |

### Métodos de Objeto

#### String (texto)
```python
# Python
texto.upper()
texto.lower()
texto.capitalize()
texto.title()
texto.strip()
texto.split()
texto.replace()
texto.find()
texto.startswith()
texto.endswith()
texto.isdigit()
texto.isalpha()
texto.isalnum()

# Pytão
texto.maiuscula()
texto.minuscula()
texto.capitalizar()
texto.titulo()
texto.removerespacos()
texto.dividir_()
texto.substituir()
texto.encontrar()
texto.comecacom()
texto.terminacom()
texto.ehdigito()
texto.ehalfa()
texto.ehalfanum()
```

#### List (lista)
```python
# Python
lista.append()
lista.extend()
lista.insert()
lista.remove()
lista.pop()
lista.clear()
lista.index()
lista.count()
lista.sort()
lista.reverse()
lista.copy()

# Pytão
lista.adicionar_()
lista.estender()
lista.inserir()
lista.remover()
lista.retirar()
lista.limpar()
lista.indice()
lista.contar()
lista.ordenar()
lista.inverter()
lista.copiar()
```

#### Dict (dicionario)
```python
# Python
dicionario.keys()
dicionario.values()
dicionario.items()
dicionario.get()
dicionario.update()
dicionario.setdefault()

# Pytão
dicionario.chaves()
dicionario.valores()
dicionario.itens()
dicionario.obter()
dicionario.atualizar()
dicionario.definirpadrao()
```

### Exceções

| Python | Pytão |
|--------|-------|
| `Exception` | `Excecao` |
| `ValueError` | `ErroValor` |
| `TypeError` | `ErroTipo` |
| `KeyError` | `ErroChave` |
| `IndexError` | `ErroIndice` |
| `AttributeError` | `ErroAtributo` |
| `NameError` | `ErroNome` |
| `FileNotFoundError` | `ErroArquivoNaoEncontrado` |
| `ZeroDivisionError` | `ErroDivisaoPorZero` |
| `ImportError` | `ErroImportacao` |
| `RuntimeError` | `ErroExecucao` |
| `NotImplementedError` | `NaoImplementado` |
| `StopIteration` | `PararIteracao` |
| `KeyboardInterrupt` | `InterrupcaoTeclado` |

### Biblioteca Padrão

#### os
```python
# Python
os.listdir()
os.mkdir()
os.rmdir()
os.path.exists()
os.path.join()

# Pytão
listardir()
criardir()
removedir()
caminho.existe()
caminhounir()
```

#### sys
```python
# Python
sys.argv
sys.path
sys.exit()

# Pytão
argumentos
caminho
sair()
```

#### datetime
```python
# Python
datetime.now()
datetime.today()
datetime.date()
datetime.time()

# Pytão
agora()
hoje()
data()
hora()
```

#### math
```python
# Python
math.sqrt()
math.pi
math.ceil()
math.floor()

# Pytão
raizquadrada()
pi
teto()
piso()
```

#### random
```python
# Python
random.random()
random.choice()
random.randint()

# Pytão
aleatorio()
escolher()
intaleatorio()
```

#### json
```python
# Python
json.loads()
json.dumps()
json.load()
json.dump()

# Pytão
carregartexto()
despejartexto()
carregar()
despejar()
```

#### re
```python
# Python
re.match()
re.search()
re.findall()
re.sub()

# Pytão
combinar()
buscar()
encontrartodos()
sub()
```

## Exemplos de Conversão

### Exemplo 1: Função Simples

```python
# Python
def saudacao(nome):
    print(f"Olá, {nome}!")
    return len(nome)

# Pytão
def saudacao(nome):
    imprimir(f"Olá, {nome}!")
    retorne tamanho(nome)
```

### Exemplo 2: Classe

```python
# Python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

# Pytão
classe Pessoa:
    def __iniciar__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __texto__(self):
        retorne f"{self.nome}, {self.idade} anos"
```

### Exemplo 3: Tratamento de Exceções

```python
# Python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero")
finally:
    print("Fim da operação")

# Pytão
tente:
    resultado = 10 / 0
exceto ErroDivisaoPorZero:
    imprimir("Erro: divisão por zero")
finalmente:
    imprimir("Fim da operação")
```

### Exemplo 4: List Comprehension

```python
# Python
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros if x % 2 == 0]

# Pytão
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 para x em numeros se x % 2 == 0]
```

### Exemplo 5: Métodos Encadeados

```python
# Python
resultado = "  Olá Mundo  ".strip().upper().replace("MUNDO", "Pytão")

# Pytão
resultado = "  Olá Mundo  ".removerespacos().maiuscula().substituir("MUNDO", "Pytão")
```

### Exemplo 6: Biblioteca Padrão

```python
# Python
import os
import json
import math

caminho = os.path.join("pasta", "arquivo.txt")
if os.path.exists(caminho):
    with open(caminho) as f:
        dados = json.load(f)

raiz = math.sqrt(16)

# Pytão
importe os
importe json
importe math

caminho = caminhounir("pasta", "arquivo.txt")
se existir(caminho):
    com abrir(caminho) como f:
        dados = carregar(f)

raiz = raizquadrada(16)
```

## Dicas de Migração

1. **Use `py2pt`** para converter código Python automaticamente
2. **Verifique o resultado** - nem sempre a tradução é perfeita
3. **Nomes de bibliotecas** continuam em inglês
4. **Strings e comentários** são preservados
5. **Docstrings** são preservadas

## Limitações

- Bibliotecas externas usam API em inglês
- Algumas traduções podem não ser idiomáticas
- Syntax errors em Pytão mostram linha do arquivo gerado