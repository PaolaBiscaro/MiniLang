## ASSIGN — Operador de atribuição

Esta categoria reconhece o símbolo de atribuição `=`

### Exemplos aceitos

"="

### Definição matemática

LAssign = {"="}

### Conjuntos auxiliares

ΣAssign = {"="}

### Expressão regular formal

rAssign = "="

### Regex de Python

r"[=]"

### Ação futura do lexer

Ao reconhecer o símbolo `=` pertencente a LAssign, o sistema vai emitir um
token Assign identificando aquele símbolo.

### Testes e interações

| Entrada | Resultado | Tipo | Justificativa |
| --- | --- | --- | --- |
| `"="` | Aceita | Fronteira | É a única palavra de LAssign e contém um símbolo. |
| `""` | Rejeita | Fronteira | A palavra vazia não contém o operador. |
| `"=="` | Rejeita | Interação | Não é uma palavra de LAssign; seu tratamento no lexer depende das demais regras. |
| `"==="` | Rejeita | Inválido | Possui três símbolos; ASSIGN reconhece apenas um por palavra. |
| `"+"` | Rejeita | Interação | Pertence à categoria de operadores aritméticos, não a ASSIGN. |
| `"+="` | Rejeita | Interação | Não é um único operador desta categoria. |
| `" ="` | Rejeita | Interação | O espaço inicial não faz parte da palavra ASSIGN. |
| `"= "` | Rejeita | Interação | O espaço final impede a correspondência da entrada inteira. |
| `"x=1"` | Rejeita | Interação | A entrada completa não é apenas o operador `=`. |
| `"=\n"` | Rejeita | Interação | A quebra de linha é um caractere adicional. |
