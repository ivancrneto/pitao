# Exemplos Práticos

> Exemplos de código em Pytão para diversos casos de uso.

## Olá Mundo

```python
# ola_mundo.pt
def ola_mundo():
    imprimir("Olá, Mundo!")

se __nome__ == "__principal__":
    ola_mundo()
```

Execute:
```bash
pytão ola_mundo.pt
# Saída: Olá, Mundo!
```

## Controle de Fluxo

### Condicional

```python
# condicional.pt
idade = inteiro(entrada("Sua idade: "))

se idade >= 18:
    imprimir("Você é maior de idade.")
senaose idade >= 12:
    imprimir("Você é adolescente.")
senao:
    imprimir("Você é criança.")
```

### Loop

```python
# loop.pt
para i em intervalo(5):
    imprimir(f"Contagem: {i}")

numeros = [1, 2, 3, 4, 5]
para num em numeros:
    se num % 2 == 0:
        imprimir(f"{num} é par")
```

### While

```python
# while.pt
contador = 0
enquanto contador < 5:
    imprimir(f"Contando: {contador}")
    contador = contador + 1
```

## Funções

### Função Simples

```python
# funcao.pt
def saudar(nome):
    retorne f"Olá, {nome}!"

resultado = saudar("Maria")
imprimir(resultado)
```

### Função com Valor Padrão

```python
# funcao_padrao.pt
def cumprimentar(nome, saudacao="Olá"):
    retorne f"{saudacao}, {nome}!"

imprimir(cumprimentar("João"))
imprimir(cumprimentar("Maria", "Bom dia"))
```

### Função com *args e **kwargs

```python
# funcao_args.pt
def somar_tudo(*numeros):
    retorne soma(numeros)

imprimir(somar_tudo(1, 2, 3, 4, 5))
```

## Classes (OOP)

### Classe Simples

```python
# pessoa.pt
classe Pessoa:
    def __iniciar__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __texto__(self):
        retorne f"{self.nome}, {self.idade} anos"
    
    def aniversario(self):
        self.idade = self.idade + 1
        retorne self.idade

pessoa = Pessoa("Carlos", 25)
imprimir(pessoa)
pessoa.aniversario()
imprimir(f"Nova idade: {pessoa.idade}")
```

### Herança

```python
# heranca.pt
classe Animal:
    def __iniciar__(self, nome):
        self.nome = nome
    
    def falar(self):
        imprimir("...")

classe Cao(Animal):
    def falar(self):
        imprimir(f"{self.nome} diz: Au au!")

classe Gato(Animal):
    def falar(self):
        imprimir(f"{self.nome} diz: Miau!")

cao = Cao("Rex")
gato = Gato("Felix")
cao.falar()
gato.falar()
```

## Tratamento de Exceções

```python
# excecoes.pt
tente:
    numero = inteiro(entrada("Digite um número: "))
    resultado = 10 / numero
    imprimir(f"Resultado: {resultado}")
exceto ErroValor:
    imprimir("Erro: número inválido")
exceto ErroDivisaoPorZero:
    imprimir("Erro: divisão por zero")
exceto:
    imprimir("Erro desconhecido")
finalmente:
    imprimir("Operação terminada")
```

## Listas e List Comprehension

```python
# listas.pt
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension
quadrados = [x**2 para x em numeros]
impares = [x para x em numeros se x % 2 != 0]

# Métodos
lista_numeros = lista([3, 1, 4, 1, 5, 9, 2, 6])
lista_numeros.ordenar()
imprimir(lista_numeros)

# Filtrar
numeros_pares = filtrar(lambda x: x % 2 == 0, numeros)
imprimir(lista(numeros_pares))
```

## Dicionários

```python
# dicionarios.pt
pessoa = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessar
imprimir(pessoa["nome"])

# Métodos
imprimir(pessoa.chaves())
imprimir(pessoa.valores())
imprimir(pessoa.itens())

# Adicionar/Atualizar
pessoa["profissao"] = "Engenheira"
pessoa.atualizar({"idade": 31})
```

## Trabalhando com Arquivos

```python
# arquivos.pt
# Escrever
usando abrir("teste.txt", "w") como arquivo:
    arquivo.escrever("Olá, arquivo!")

# Ler
usando abrir("teste.txt", "r") como arquivo:
    conteudo = arquivo.ler()
    imprimir(conteudo)
```

## Módulos e Imports

```python
# imports.pt
importe os
importe math
importe json

# Usando stdlib
pasta = "documents"
se caminho.ehdir(pasta):
    arquivos = listardir(pasta)
    imprimir(f"Arquivos em {pasta}: {tamanho(arquivos)}")

# Math
imprimir(f"Raiz de 16: {raizquadrada(16)}")
imprimir(f"Pi: {pi}")

# JSON
dados = {"nome": "João", "idade": 25}
json_str = despejartexto(dados)
imprimir(f"JSON: {json_str}")
```

## Expressões Regulares

```python
# regex.pt
importe re

texto = "Meu email é exemplo@email.com e outro@teste.org"

# Buscar email
email = buscar(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto)
se email:
    imprimir(f"Email encontrado: {email.grupo()}")

# Encontrar todos os emails
emails = encontrartodos(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto)
para email em emails:
    imprimir(f"Email: {email}")

# Substituir
novo_texto = sub(r"@email\.com", "@novo.com", texto)
imprimir(f"Texto modificado: {novo_texto}")
```

##日期 e Hora

```python
# datetime_exemplo.pt
importe datetime

agora = agora()
imprimir(f"Data e hora atual: {agora}")

data_atual = hoje()
imprimir(f"Data de hoje: {data_atual}")
```

## Generators e Yield

```python
# generator.pt
def contador(max):
    i = 0
    enquanto i < max:
        produza i
        i = i + 1

para num em contador(5):
    imprimir(f"Número: {num}")
```

## Decorators

```python
# decorator.pt
def meu_decorator(func):
    def wrapper(*args, **kwargs):
        imprimir("Antes da função")
        resultado = func(*args, **kwargs)
        imprimir("Depois da função")
        retorne resultado
    retorne wrapper

@meu_decorator
def dizer_oi():
    imprimir("Olá!")

dizer_oi()
```

## Context Managers (with)

```python
# context_manager.pt
importe io

# Arquivo
usando abrir("dados.txt", "w") como f:
    f.escrever("Dados salvos")

# StringIO (exemplo)
buffer = io.StringIO()
usando abrir("temp.txt", "w") como arquivo:
    arquivo.escrever("texto")
```

## Debugging

```python
# debug.pt
def dividir(a, b):
    imprimir(f"Dividindo {a} por {b}")
    se b == 0:
        imprimir("Aviso: divisor é zero!")
        retorne Nulo
    retorne a / b

resultado = dividir(10, 2)
imprimir(f"Resultado: {resultado}")

resultado_nulo = dividir(10, 0)
imprimir(f"Resultado nulo: {resultado_nulo}")
```

## Exemplo Completo: Lista de Tarefas

```python
# tarefas.pt
classe Tarefa:
    def __iniciar__(self, titulo, concluida=Falso):
        self.titulo = titulo
        self.concluida = concluida
    
    def __texto__(self):
        status = "[x]" se self.concluida senao "[ ]"
        retorne f"{status} {self.titulo}"
    
    def marcar_concluida(self):
        self.concluida = Verdadeiro

tarefas = [
    Tarefa("Aprender Pytão"),
    Tarefa("Escrever código"),
    Tarefa("Criar projeto")
]

# Listar
para i, tarefa em enumerate(tarefas):
    imprimir(f"{i + 1}. {tarefa}")

# Marcar como concluída
tarefas[0].marcar_concluida()

# Filtrar pendentes
pendentes = [t para t em tarefas se nao t.concluida]
imprimir(f"\nTarefas pendentes: {tamanho(pendentes)}")
```

## Conversão de Código

Você pode converter qualquer arquivo Python para Pytão:

```bash
# Converter Python para Pytão
py2pt script.py -o script.pt

# Converter Pytão para Python  
pt2py script.pt -o script.py
```

Exemplo de conversão:

```python
# Python original (script.py)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Convertido para Pytão (script.pt)
def fibonacci(n):
    se n <= 1:
        retorne n
    retorne fibonacci(n-1) + fibonacci(n-2)

para i em intervalo(10):
    imprimir(f"F({i}) = {fibonacci(i)}")
```