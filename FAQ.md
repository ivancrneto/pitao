# Perguntas Frequentes (FAQ)

## O que é Pytão?

Pytão é um **pré-processador** que permite escrever código Python usando palavras em português. O código é traduzido automaticamente para Python antes da execução.

> **Nota:** Pytão não é uma linguagem de programação diferente. É uma ferramenta de tradução que facilita a escrita de Python para falantes de português.

## Pytão é Python?

**Não.** Pytão é uma ferramenta de tradução. Tecnicamente:

1. Você escreve código em português (`.pt`)
2. O pré-processador traduz para Python (`.py`)
3. O Python é executado normalmente

**O resultado final é sempre Python real.**

## Por que usar Pytão?

### Para iniciantes:
- Reduce a barreira linguística
- Foca na lógica antes da sintaxe
- Material didático em português

### Para educação:
- Aulas de programação em português
- Exercícios mais acessíveis
- Feedback em português

### Para prototipagem:
- Scripts rápidos em português
- Automação de tarefas simples

## Quando NÃO usar Pytão?

- ❌ Em código de produção
- ❌ Projetos com outros desenvolvedores
- ❌ Bibliotecas ou pacotes
- ❌ Quando precisa de suporte de comunidade

**Python padrão é sempre recomendado para projetos reais.**

## Posso usar bibliotecas Python?

**Sim!** Bibliotecas são importadas normalmente:

```python
# Funciona perfeitamente
importe numpy como np
importe pandas como pd
importe requests

dados = np.array([1, 2, 3])
resposta = requests.obter("https://api.exemplo.com")
```

As bibliotecas mantêm seus nomes e API em inglês.

## Como funciona a tradução?

```
┌─────────────────┐
│   código.pt      │
│  (português)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   pré-processador   │
│   (Pytão)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   código.py     │
│   (Python)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Python        │
│   Runtime       │
└─────────────────┘
```

## Posso converter código Python existente?

**Sim!** Use `py2pt`:

```bash
py2pt meu_script.py -o meu_script.pt
```

## E o contrário? Converter Pytão para Python?

**Sim!** Use `pt2py`:

```bash
pt2py meu_script.pt -o meu_script.py
```

## Quais versões de Python são suportadas?

Python 3.8, 3.9, 3.10, 3.11, 3.12 e 3.13.

## Posso usar Pytão com IDEs?

### VS Code

Instale a extensão `vscode-pitao` para:
- Syntax highlighting
- Snippets
- IntelliSense básico

### Outros IDEs

O código `.pt` é tratado como texto simples. Configure:
- Identificação de linguagem como Python
- Formatting com Python

## Como reportar bugs?

1. Verifique se o código Python gerado está correto
2. Teste o código Python original
3. Abra uma issue com:
   - Código original (.pt)
   - Código traduzido (.py)
   - Erro retornado

## Posso contribuir?

**Sim!** Contributions são bem-vindas:

1. Fork o repositório
2. Crie uma branch (`feat/nova-feature`)
3. Implemente com testes
4. Abra um Pull Request

## Quais são as limitações?

1. **Bibliotecas externas** - API sempre em inglês
2. **Syntax errors** - Mostram linha do arquivo gerado
3. **Debugging** - Pode ser confuso com linhas traduzidas
4. **Type hints** - Não são traduzidos

## Como Pytão se compara a outras linguagens?

| Linguagem | Descrição |
|-----------|-----------|
| Python | Linguagem real, palavras em inglês |
| **Pytão** | **Tradução português → Python** |
| Bython | Inspiração, mesma abordagem |
| CoffeeScript | Traduz para JavaScript |

## Posso usar Pytão em produção?

**Não recomendamos.** Pytão é uma ferramenta de:
- Aprendizagem
- Prototipagem
- Educação

Para produção, use Python padrão.

## O código é executado diretamente?

Não. Sempre há uma tradução:

1. `pytão script.pt` → Gera `script.py` → Executa Python
2. `pytão -c script.pt` → Só gera `script.py`
3. `pytão -k script.pt` → Gera e executa, mantém `.py`

## Posso usar palavras em inglês junto?

**Sim!** O código pode misturar:

```python
# Mistura válida
def hello_world():
    print("Hello")  # palavra em inglês
    imprimir("World")  # palavra em português
```

Ambas funcionam.

## Como escolher nomes de traduções?

As traduções foram escolhidas seguindo:
1. **Clareza** - Nome em português claro
2. **Consistência** - Padrão nomeado
3. **Curto** - Não muito longo
4. **Português brasileiro** - Preferencialmente

Exemplos:
- `print` → `imprimir` (ação clara)
- `len` → `tamanho` (significado claro)
- `True`/`False` → `Verdadeiro`/`Falso` (direto)

## Onde posso aprender Python "real"?

Após aprender com Pytão, migrar para Python é natural:

1. [Documentação Python](https://docs.python.org/pt-br/)
2. [Tutorial Python](https://docs.python.org/pt-br/3/tutorial/)
3. [Coursera](https://www.coursera.org/specializations/python)
4. [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)

## Contato e Suporte

- GitHub Issues: Para bugs e features
- Discussions: Para perguntas
- README: Documentação geral

---

**Lembre-se:** Pytão é uma ferramenta de tradução, não um substituto para Python!