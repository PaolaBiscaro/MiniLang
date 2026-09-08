# MiniLang
Integrantes :
Lucas Hygidio - 1996610
Paola Biscaro - 2005412
Lorena de Souza - 1996291
Heloísa Ribeiro - 1992348

---
## Tabela das 11 classes:

| Classe | O que reconhece | Exemplos aceitos | Ação futura do lexer |
| --- | --- | --- | --- |
| `KEYWORD_CORE` | Palavras reservadas do núcleo | `int`, `print` | Emitir o token da palavra reservada |
| `IDENT_BASE` | Palavras que seguem o padrão de identificadores: começam com letra ASCII ou `_`, seguidas de letras ASCII, dígitos ou `_` | `valor`, `_contador`, `total2` | Verificar se é palavra reservada; caso contrário, emitir `IDENT` |
| `INT_LITERAL` | Sequências de um ou mais dígitos de `0` a `9`, com zeros à esquerda permitidos | `0`, `007`, `123` | Emitir `INT_LITERAL` |
| `ASSIGN` | Operador de atribuição | `=` | Emitir `ASSIGN` |
| `ARITH_OP` | Operadores aritméticos | `+`, `-`, `*`, `/` | Emitir `PLUS`, `MINUS`, `STAR` ou `SLASH` |
| `DELIMITER_CORE` | Delimitadores do núcleo | `(`, `)`, `;` | Emitir `LPAREN`, `RPAREN` ou `SEMICOLON` |
| `LINE_COMMENT` | Comentários iniciados por `//`, encerrados antes de CR (`\r`) ou NL (`\n`) | `//`, `// comentário` | Reconhecer e ignorar |
| `WHITESPACE` | Uma ou mais ocorrências de espaço, tabulação ou quebra de linha | `" "`, `"\t"`, `"\r\n"` | Reconhecer e ignorar |
| `KEYWORD_EXT` | Palavras reservadas da extensão | `if`, `else`, `while` | Emitir o token da palavra reservada |
| `REL_OP` | Operadores relacionais | `<`, `<=`, `>`, `>=`, `==`, `!=` | Emitir o token do operador relacional |
| `BLOCK_DELIMITER` | Delimitadores de bloco | `{`, `}` | Emitir o token de abertura ou fechamento de bloco |

## Documentação das classes
### Identificadores
- [Documentação](https://github.com/PaolaBiscaro/MiniLang/blob/main/documentation/identificadores.md)
- [Código](https://github.com/PaolaBiscaro/MiniLang/blob/main/reconhecedores/identifiers.py)

### Comentários
- [Documentação](https://github.com/PaolaBiscaro/MiniLang/blob/main/documentation/comentarios.md)
- [Código](https://github.com/PaolaBiscaro/MiniLang/blob/main/reconhecedores/line_comment.py)

### Comparações
- [Documentação](https://github.com/PaolaBiscaro/MiniLang/blob/main/documentation/comparacoes.md)
- [Código](https://github.com/PaolaBiscaro/MiniLang/blob/main/reconhecedores/comparison.py)

### Delimitadores
- [Documentação](https://github.com/PaolaBiscaro/MiniLang/blob/main/documentation/delimitadores.md)
- [Código](https://github.com/PaolaBiscaro/MiniLang/blob/main/reconhecedores/delimiter.py)

### Espaços em branco
- [Documentação](https://github.com/PaolaBiscaro/MiniLang/blob/main/documentation/espacoBranco.md)
- [Código](https://github.com/PaolaBiscaro/MiniLang/blob/main/reconhecedores/whitespace.py)

### Literias inteiros
- [Documentação](https://github.com/PaolaBiscaro/MiniLang/blob/main/documentation/literais_inteiros.md)
- [Código](https://github.com/PaolaBiscaro/MiniLang/blob/main/reconhecedores/intLiteral.py)

### Operador de atribuição
- [Documentação](https://github.com/PaolaBiscaro/MiniLang/blob/main/documentation/operadorAtribuicao.md)
- [Código](https://github.com/PaolaBiscaro/MiniLang/blob/main/reconhecedores/rAssign.py)

### Operadores aritméticos
- [Documentação](https://github.com/PaolaBiscaro/MiniLang/blob/main/documentation/operadoresAritmeticos.md)
- [Código](https://github.com/PaolaBiscaro/MiniLang/blob/main/reconhecedores/rArith.py)

## Interações entre classes

Resumo dos resultados esperados para as oito interações no lexer futuro.

| Caso | Entradas | Resultado |
| --- | --- | --- |
| `KEYWORD_CORE × IDENT_BASE` | `int`, `intx`, `print`, `print2` | `int` e `print` são palavras reservadas; `intx` e `print2` são identificadores. |
| `KEYWORD_EXT × IDENT_BASE` | `if`, `ifx`, `else2`, `while1` | `if` é palavra reservada; `ifx`, `else2` e `while1` são identificadores. |
| `ASSIGN × REL_OP` | `=`, `==`, `===` | `=` é atribuição; `==` é comparação; `===` não é um único operador dessas classes. |
| `ARITH_OP × LINE_COMMENT` | `/`, `//`, `//x` | `/` é divisão; `//` e `//x` são comentários e serão ignorados. |
| Prefixos de `REL_OP` | `<`, `<=`, `>`, `>=`, `!`, `!=` | `<`, `<=`, `>`, `>=` e `!=` são operadores relacionais; `!` sozinho é rejeitado. |
| `ARITH_OP × INT_LITERAL` | `-10`, `+7` | `-10` forma `MINUS` e `INT_LITERAL`; `+7` forma `PLUS` e `INT_LITERAL`. O sinal não pertence ao inteiro. |
| Delimitadores adjacentes | `()`, `{}`, `);` | `()` forma `LPAREN` e `RPAREN`; `{}` forma `LCHAVE` e `RCHAVE`; `);` forma `RPAREN` e `SEMICOLON`. |
| Classes ignoradas | Espaços e comentários entre tokens | O lexer reconhece e ignora esses trechos, preservando os demais tokens. |

## Execução dos testes

Na pasta do projeto, execute:

```sh
python3 testes.py
```

O programa imprime oito dicionários com os retornos dos reconhecedores,
agrupando as 11 classes. Essas listas permitem conferir os resultados de cada
palavra; seus retornos são preservados: nomes de tokens, `None`, `"REJECTED"`
ou valores booleanos, conforme o reconhecedor.

As oito listas ficam em `testes.py`, uma por linha, e incluem palavras
válidas, inválidas, fronteiras do slide 97 e entradas das interações do
slide 98. Os resultados são exibidos para conferência.

O reconhecimento com `fullmatch` verifica a entrada inteira como um único
lexema. Assim, `-10` é recusado como um único inteiro e `()` como um único
delimitador. As funções não separam frases em tokens; as decisões do lexer
futuro estão descritas na tabela de interações acima.

### Testar uma lista de palavras

As funções `test_rArith`, `test_rAssign`, `test_rel_op`,
`test_classify_delimiter`, `test_classify_ident`, `test_classify_int_literal`,
`test_identify_and_ignores_line_comment` e `test_identify_and_ignore_whitespace`
recebem uma lista e devolvem `{palavra: retorno_do_reconhecedor}`.

```python
from testes import test_rArith, test_classify_int_literal

palavras = ["+", "-", "*", "/", "//", ""]
print(test_rArith(palavras))
# {'+': 'PLUS', '-': 'MINUS', '*': 'STAR', '/': 'SLASH', '//': None, '': None}

print(test_classify_int_literal(["007", "-10", "12a"]))
# {'007': 'INT_LITERAL', '-10': None, '12a': None}
```

Palavras repetidas em uma lista ocupam uma única chave no dicionário.
