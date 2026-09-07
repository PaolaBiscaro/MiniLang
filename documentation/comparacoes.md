## REL_OP — Operadores relacionais

Esta categoria reconhece os símbolos utilizados para operações de comparação lógica: `<`, `>`, `<=`, `>=`, `==` e `!=`.

### Exemplos aceitos

"<", ">", "<=", ">=", "==", "!="

### Definição matemática

LRelOp = {"<", ">", "<=", ">=", "==", "!="}

### Conjuntos auxiliares

ΣRelOp = {"<", ">", "=", "!"}

### Expressão regular formal

rRelOp = (< | >) (=)? | = = | ! =

### Regex de Python

r"[<>]=?|==|!="

### Ação futura do lexer

Ao reconhecer um dos símbolos pertencentes a LRelOp, o sistema vai emitir um
token RelOp identificando aquele operador lógico.

### Testes e interações

| Entrada | Resultado | Tipo | Justificativa |
| --- | --- | --- | --- |
| `"<="` | Aceita | Comum | É uma palavra válida de LRelOp composta por dois símbolos válidos e na ordem certa. |
| `">"` | Aceita | Fronteira | É a menor correspondência válida do grupo de grandeza. |
| `"=="` | Aceita | Fronteira | Palavra de LRelOp que exige exatamente dois caracteres de igualdade. |
| `"="` | Rejeita | Interação | Não pertence a LRelOp. É um operador de atribuição (ASSIGN) e falha na verificação de `==`. |
| `"!"` | Rejeita | Interação | Não pertence a LRelOp. Pode ser um operador de negação unária, mas falha pois falta o `=`. |
| `""` | Rejeita | Fronteira | A palavra vazia não contém nenhum operador. |
| `"=>"` | Rejeita | Inválido | A ordem dos caracteres está invertida (o correto para a MiniLang é `>=`). |
| `"==="` | Rejeita | Inválido | Possui três símbolos; REL_OP reconhece no máximo dois por palavra. |
| `"<=="` | Rejeita | Inválido | Excesso de caracteres de atribuição combinados com o operador de grandeza. |
| `" =="` | Rejeita | Interação | O espaço inicial não faz parte da palavra REL_OP. |
| `"!= "` | Rejeita | Interação | O espaço final impede a correspondência da entrada inteira. |
| `"x>y"` | Rejeita | Interação | A entrada completa contém operandos (`x` e `y`). A regex léxica isola apenas o operador. |