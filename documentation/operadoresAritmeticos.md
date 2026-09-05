## ARITH — Operadores aritméticos

Esta categoria reconhece os símbolos de adição (`+`), subtração (`-`),
multiplicação (`*`) e divisão (`/`).

### Exemplos aceitos

Como a linguagem é finita, todas as palavras aceitas são enumeradas:

"+"
"-"
"/"
"*"

### Definição matemática

LArith = {"+", "-", "*", "/"}

### Conjuntos auxiliares

ΣArith = {"+", "-", "*", "/"}

### Expressão regular formal


rArith = "+" ∪ "-" ∪ "*" ∪ "/"

### Regex de Python

r"[+*/-]"

### Ação futura do lexer

Ao reconhecer um simbolo pertencente ao conjunto do LArtith o sistema vai emitir um 
token Arith identificando aquele simbolo 

### Testes e interações

| Entrada | Resultado | Tipo | Justificativa |
| --- | --- | --- | --- |
| `"+"` | Aceita | Fronteira | Uma palavra válida tem exatamente um símbolo. |
| `"-"` | Aceita | Comum | É o símbolo de subtração. |
| `"*"` | Aceita | Comum | É o símbolo de multiplicação. |
| `"/"` | Aceita | Comum | É o símbolo de divisão. |
| `""` | Rejeita | Fronteira | A palavra vazia não contém um operador. |
| `"++"` | Rejeita | Fronteira | Possui dois símbolos; ARITH reconhece apenas um por palavra. |
| `"//"` | Rejeita | Interação | Não é uma palavra de LArith; seu tratamento no lexer depende das demais regras. |
| `"**"` | Rejeita | Inválido | O operador composto não está no conjunto enumerado. |
| `"+="` | Rejeita | Interação | Não é um único operador desta categoria. |
| `"="` | Rejeita | Interação | Pertence à categoria de atribuição, não a ARITH. |
| `" +"` | Rejeita | Interação | O espaço inicial não faz parte da palavra ARITH. |
| `"+ "` | Rejeita | Interação | O espaço final impede a correspondência da entrada inteira. |
| `"+\n"` | Rejeita | Interação | A quebra de linha é um caractere adicional. |
| `"1+2"` | Rejeita | Interação | A entrada inteira contém operandos e operador, não apenas uma palavra ARITH. |
