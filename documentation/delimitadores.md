# Delimitadores

## DELIMITER_CORE
### Classe e finalidade
Reconhece todo caractere que seja unicamente "(", ")", ";" 

### Descrição informal
Identifica apenas a ocorrencia de um único caracter, e retorna a sua classificação. Não é permitido a inserção de mais caracteres parecidos sendo rejeitados.

### Exemplos que são aceitos
"(", ")", ";"

### Definição matemática
LDelimiterCore =  {"(", ")", ";"}

### Expressão regular formal
rDelimitadores = "(" U ")" U ";"

### Regex de Python
``` python
r"[();]"
```

### Ação futura do lexer
Após identificar um delimitador, o lexer gera e envia o token correspondente (RPAREN, LPAREN ou SEMICOLON) para o parser e avança a leitura para o próximo caractere.

### Testes e interações

| Entrada |  Obtido | Categoria | Justificativa |
| :--- | :--- | :--- | :--- |
| ( | LPAREN | Fronteira | Menor palavra possivel para a classificação LPAREN|
| ) | LPAREN | Fronteira | Menor palavra possivel para a classificação RPAREN|
| ; | SEMICOLON | Fronteira | Menor palavra possivel para a classificação SEMICOLON |
| ;; | REJECTED | Não pertence | Não corresponde a nenhum token |
| () | REJECTED | Não pertence | Corresponde a dois tokens simultaneamente, é uma palavra invalida por possuir dois lexemas |
| valor; | REJECTED | Não pertence | Não corresponde a nenhum token nesse contexto |


## BLOCK_DELIMITER
### Classe e finalidade
Reconhece todo caractere que seja unicamente "{", "}"

### Descrição informal
Identifica apenas a ocorrencia de um único caracter, e retorna a sua classificação. Não é permitido a inserção de mais caracteres parecidos sendo rejeitados.

### Exemplos que são aceitos
"{", "}"

### Definição matemática
LBlockDelimiter =  {"{", "}"}

### Expressão regular formal
rDelimitadores = "{" U "}"

### Regex de Python
``` python
r"[{}]"
```

### Ação futura do lexer
Após identificar um delimitador, o lexer gera e envia o token correspondente (RCHAVE ou LCHAVE) para o parser e avança a leitura para o próximo caractere.

### Testes e interações

| Entrada |  Obtido | Categoria | Justificativa |
| :--- | :--- | :--- | :--- |
| { | LCHAVE | Fronteira | Menor palavra possivel para a classificação LCHAVE |
| } | RCHAVE | Fronteira | Menor palavra possivel para a classificação RCHAVE |
| {} | REJECTED | Não pertence | Corresponde a dois tokens simultaneamente, é uma palavra invalida por possuir dois lexemas |
| function{} | REJECTED | Não pertence | Não corresponde a nenhum token nesse contexto. |
