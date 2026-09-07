# Comentários

## LINE_COMMENT
### Classe e finalidade
Reconhece e ignora (descarta) a sequência de caracteres pertencentes a um comentário de linha.

### Descrição informal
Começa com "//" e finaliza antes do  "\n", sendo que pode haver  qualquer caractere entre o inicio e o fim. A quebra de linha é devolvida para facilitar a identificacao de outros blocos de texto.

### Exemplos que são aceitos
"//comentario", "// // outro comentario", "// \n"

### Definição matemática
LLineComment = // C* 

### Expressão regular formal
rComentário = // C*

### Conjuntos que são auxiliares
C = ΣFonte - {CR, NL}

### Regex de Python
``` python
r"//[^\r\n]*"
```

### Ação futura do lexer
Após o comentário ser descartado, o objetivo do lexer é retornar ao laço de leitura para realizar o processamento novamente.

### Testes e interações

| Entrada | Esperado | Obtido | Categoria | Justificativa |
| :--- | :--- | :--- | :--- | :--- |
| //comentario \n | IGNORED | "\n " | Comum | Tem o // seguido de alguns caracteres e por fim, finaliza com o \n |
| // | IGNORED | "" | Fronteira | Tem somente o // sendo a menor palavra possivel|
| // // | IGNORED | "" | Fronteira | Possui uma repeticao do // sendo ignorado tambem |
| int valor; //comentario | IGNORED THE COMMENT | "int valor;" | Comum | Possui outro texto antes do comentario, que é retornado. |
| //comentario \n int variavel | IGNORED THE COMMENT | "\n int variavel" | Comum | Possui outras palavras após a quebra de linha.  |
| //\n | IGNORED | " \n" | Fronteira | Tem o // seguido do \n |
