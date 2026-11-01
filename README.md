# MiniLang

Integrantes:
Lucas Hygidio - 1996610,
Paola Biscaro - 2005412,
Lorena de Souza - 1996291,
Heloísa Ribeiro - 1992348.

---
## Executando o projeto

Na pasta principal do projeto execute:

```sh
python main.py
```

O programa lê o código-fonte que está na pasta `arquivo-txt/programa.txt`, realiza a análise léxica e sintática e exibe a AST (Abstract Syntax Tree), ou Árvore Sintática Abstrata. Se encontrar um caractere inválido ou um erro de sintaxe, mostra o diagnóstico correspondente.

Exemplo de saída:

```
Programa
├── Declaracao(x)
├── Atribuicao(x)
│   └── Binaria(+)
│       ├── Inteiro(2)
│       └── Binaria(/)
│           ├── Inteiro(3)
│           └── Inteiro(1)
└── Saida
    └── Variavel(x)
```

A AST é organizada a partir da raiz, de cima para baixo. O nó **Programa** reúne os comandos na mesma ordem em que aparecem no código: `declaração`, `atribuição` e `saída`.

Exemplo de um programa no arquivo-txt/programa.txt:

```sh
int x;
x = 2 + 3 / 1;
print(x);
```

- **Declaração:** ``int x;``
- **Atribuição:** ``x = 2 + 3 / 1;``
- **Saída:** ``print(x);``




## Interações entre o lexer e o Parser

O lexer transforma o texto em tokens. O Parser recebe esses tokens, verifica se estão na ordem esperada e, se estiverem, constrói a AST - Árvore Sintática Abstrata.

***OBS:** o lexer pode reconhecer alguns tokens que o Parser ainda não usa. Reconhecer um token não significa que o comando correspondente já seja válido na gramática da MiniLang.*

| Entrada | O que o lexer faz | O que o Parser faz |
| --- | --- | --- |
| `int x;` | Emite `KW_INT`, `IDENT`, `SEMICOLON` e `EOF`. | Reconhece uma declaração e cria `Declaracao(x)`. |
| `x = 2 + 3 * 4;` | Emite os tokens do identificador, da atribuição, dos números e dos operadores. | Reconhece uma atribuição e monta a expressão com `+` na raiz e `*` à direita, respeitando a precedência. |
| `print((2 + 3) * 4);` | Emite os tokens de `print`, parênteses, números e operadores. | Reconhece a saída e monta a expressão com `*` na raiz e `+` à esquerda, respeitando os parênteses. |
| `x = 6 / 2; // divisão` | Emite `SLASH` para `/` e ignora o comentário iniciado por `//`. | Reconhece a atribuição e cria um nó binário para a divisão. |
| `print(y);` | Emite tokens para `print`, parênteses e o identificador `y`. | Aceita a estrutura sintática. Não verifica se `y` foi declarada. |
| `print(2 + );` | Emite tokens válidos, incluindo `RPAREN` depois do `+`. | Gera erro sintático porque esperava um inteiro, identificador ou `(` após o operador.|
| `if (x) { print(x); }` | Reconhece `if`, os parênteses e as chaves como tokens. | Rejeita a entrada porque `if` e blocos não estão implementados na gramática atual do Parser. |

Quando houver um erro, por exemplo em `print(2 + );` será exibida a mensagem: **"Erro sintático: Linha 1, coluna 11: esperado inteiro, identificador ou "(", encontrado RPAREN (')')"**



## Tabela das 11 categorias léxicas reconhecidas

| Classe | O que reconhece | Exemplos aceitos | Tratamento pelo Lexer |
| --- | --- | --- | --- |
| `KEYWORD_CORE` | Palavras reservadas do núcleo | `int`, `print` | Emitir o token da palavra reservada |
| `IDENT_BASE` | Palavras que seguem o padrão de identificadores: começam com letra ASCII ou `_`, seguidas de letras ASCII, dígitos ou `_` | `valor`, `_contador`, `total2` | Verifica se a palavra é reservada. Caso contrário, emitir `IDENT` |
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



## Execução dos testes

### Teste dos Reconhecedores léxicos

Na pasta do projeto, execute:

```sh
python tests\testesReconhecedores.py
```

O programa imprime oito dicionários com os retornos dos reconhecedores,
agrupando as 11 classes. Essas listas permitem conferir os resultados de cada
palavra. Seus retornos são preservados: nomes de tokens, `None`, `"REJECTED"`
ou valores booleanos, conforme o reconhecedor.

As oito listas ficam em `testesReconhecedores.py`, uma por linha, e incluem palavras
válidas, inválidas, fronteiras e entradas das interações. Os resultados são exibidos para conferência.

O reconhecimento com `fullmatch` verifica a entrada inteira como um único
lexema. Assim, `-10` é recusado como um único inteiro e `()` como um único
delimitador. As funções não separam frases em tokens. 


### Testes do Parser

Na pasta do projeto, execute:

```sh
python tests\testesParser.py
```

O arquivo contém oito testes manuais. Eles verificam se o Parser reconhece declarações, atribuições e comandos print, se monta corretamente a AST - Árvore Sintática Abstrata de expressões com precedência, parênteses e associação à esquerda, se aceita sequências de comandos e programas vazios e se gera diagnósticos para entradas sintaticamente inválidas.

Para esses testes, o código-fonte passa primeiro pelo lexer, que produz os tokens recebidos pelo Parser.

O programa exibe [OK] para cada teste aprovado e [FALHOU] quando uma verificação não corresponde ao resultado esperado. Ao final, mostra a quantidade de testes aprovados. Os testes não executam as expressões nem verificam se as variáveis foram declaradas.