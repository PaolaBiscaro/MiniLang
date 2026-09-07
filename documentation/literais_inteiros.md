## LITERAL_INT — Literal Inteiro

Esta categoria reconhece valores numéricos inteiros literais, compostos exclusivamente por uma sequência de um ou mais dígitos (de 0 a 9). 

### Exemplos aceitos

"0", "42", "2026", "999999"

### Definição matemática

LLitInt = { w ∈ ΣDigit⁺ }

### Conjuntos auxiliares

ΣDigit = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

### Expressão regular formal

rLitInt = (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)⁺

### Regex de Python

r"[0-9]+"

### Ação futura do lexer

Ao reconhecer uma sequência pertencente a LLitInt, o sistema vai emitir um
token LiteralInt (ou um nome similar definido na linguagem) guardando o próprio valor numérico extraído para ser utilizado posteriormente pela análise sintática.

### Testes e interações

| Entrada | Resultado | Tipo | Justificativa |
| --- | --- | --- | --- |
| `"42"` | Aceita | Comum | É uma palavra de LLitInt composta por mais de um símbolo válido. |
| `"0"` | Aceita | Fronteira | Representa o menor comprimento possível exigido pela regra (exatamente um dígito numérico). |
| `""` | Rejeita | Fronteira | A palavra vazia não contém dígitos; o modificador `+` exige no mínimo uma ocorrência. |
| `"42.5"` | Rejeita | Interação | Contém um ponto decimal não reconhecido pela regra. (Seria um número de ponto flutuante, não um inteiro). |
| `"-10"` | Rejeita | Interação | O sinal `-` não pertence ao conjunto de dígitos. Em especificações léxicas, o `-` geralmente é lido como um token de operador unário separado do token literal `10`. |
| `"123a"` | Rejeita | Inválido | A letra `a` não faz parte de ΣDigit, quebrando a validação restrita da string inteira (`fullmatch`). |
| `" 10"` | Rejeita | Interação | O espaço no início não faz parte da palavra LITERAL_INT. |
| `"10 "` | Rejeita | Interação | O espaço no final não faz parte da palavra LITERAL_INT. |