# Espaços em Branco

## WHITESPACE
### Classe e finalidade
Reconhece e ignora (descarta) todo espaço em branco o que inclui quebras de linhas e tab.

### Descrição informal
Identifica os espacamentos e os remove. Não é aceito strings vazias.

### Exemplos que são aceitos
Qualquer sequência que contenha ao menos um espaço em branco, quebra de linha o tab.
" ", "int valor", "\n", "\t print"

### Definição matemática
B = {espaço, tab, CR, NL}
LWhitespace = B+

### Expressão regular formal
rEspaços = B+

### Conjuntos que são auxiliares
B = {ESP, TAB, CR, NL}

### Regex de Python
``` python
r'[ \t\r\n]+'
```

### Ação futura do lexer
Após os espaços em branco serem removidos, o analisador avança para a leitura para encontrar o próximo token.

### Testes e interações

| Entrada | Esperado | Obtido | Categoria | Justificativa |
| :--- | :--- | :--- | :--- | :--- |
| int valor | IGNORED | None | Comum | Contem strings comuns |
| \n | IGNORED | True | Fronteira | Contem somente uma quebra de linha |
| \n \t | IGNORED | None | Fronteira | Contem uma quebra de linha e uma tabulação |
| \n var teste | IGNORED | None | Comum | Possui outros tipos de palavras. |
| " 1 + 1" | IGNORED | None | Comum | Mantem somente o que não pertence aos espacos em branco |

