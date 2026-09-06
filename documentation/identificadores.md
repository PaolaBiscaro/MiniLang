# Identificadores e KW

## IDENT_BASE
### Classe e finalidade
Ele é o padrão base de identificadores

### Descrição informal
Começa com uma letra ou o undeline '\_' e depois pode ter letas, digitos, ou undeline '\_'

### Exemplos que são aceitos
"total2", "_contagem", "x", "\_"

### Definição matemática
$LIdentBase = Inicial Continuacao*$

### Conjuntos que são auxiliares
$Inicial = Letra \cup \text{"\_"}$

$Continuacaoo = Letra \cup Digito \cup \text{"\_"}$

### Expressão regular formal
$rIdentBase = (Letra \cup \text{"\_"}) (Letra \cup Digito \cup \text{"\_"})^*$

### Regex de Python
``` python
r"[A-Za-z_][A-Za-z0-9_]*"
```

### Ação futura do lexer
Reclassificar, caso pertencer ao KEYWORD_CORE ou KEYWORD_EXT, ele irá enviar o token da paralavra que está reservada, caso não pertencer, ele irá identificar como IDENT

### Testes e interações

| Classe | Entrada | Esperado | Obtido | Categoria | Justificativa |
| --- | --- | --- | --- | --- | --- |
| IDENT_BASE | total2 | IDENT | IDENT | Aceita | Tem letra inicial seguida de letras e digito |
| IDENT_BASE | 2valor | REJECTED | REJECTED | Rejeitado | Não pode começar com um digito |
| IDENT_BASE | _contador | IDENT | IDENT | Aceito | O underline inicial é permito como caractere inicial |
| IDENT_BASE | x | IDENT | IDENT | Fronteira | Menor identificador valido que é possivel ter |
| IDENT_BASE | "" | REJECTED | REJECTED | Fronteira | O padrão aqui exige pelo menos um caractere, não podendo ter vazio |
| IDENT_BASE | total-2 | REJECTED | REJECTED | Rejeitado | Tem um simbolo que não pertence ao alfabeto |
| IDENT_BASE | int | KW_INT | KEYWORD_INT |  Interação | Tem o padrão que se espera para os identificadores, porém ele é uma palavra reservada |
| IDENT_BASE | intx | IDENT | IDENT | Fronteira | o 'x' faz com que ele não seja uma palavra reservada e por ele, a palavra se torna um identificador comum |
| IDENT_BASE | print2 | IDENT | IDENT | Interação | Começa com a palavra reservada porém há um digito ao final que o desclassifica de ser uma palavra reservada |
| IDENT_BASE | if | KW_IF | KEYWORD_IF | Interação | Pertence a IDENT_BASE, porém ele faz parte das que são as palavras reservadas |
| IDENT_BASE | while1 | IDENT | IDENT | Interação | Adicionar dígito após palavra reservada de extensão a transforma em identificador |
| IDENT_BASE | while | KW_WHILE | KEYWORD_WHILE | Interação | Pertence a IDENT_BASE, porém ele faz parte das que são as palavras reservadas |

## KEYWORD_CORE
### Classe e finalidade
São palavras reservadas obrigatórias

### Descrição informal
Representa o conjunto restrito e especifico de palavras chaves da linguagem, usadas para declaração de tipoe comandos

### Exemplos aceitos
"int", "print"

### Definição matemática
$RCore = \{\text{"int"}, \text{"print"}\}$

### Conjuntos auxiliares
Não tem

### Expressão regular formal
$rCore = \text{"int"} \cup \text{"print"}$

### Regex em Python
``` python
r"int|print"
```

### Ação futura do lexer
Reconhece a palavra e emite o token que corresponde a palavra que é reservada (ex: KW_INT ou KW_PRINT)

### Testes e interações

| Classe | Entrada | Esperado | Obtido | Categoria | Justificativa |
| --- | --- | --- | --- | --- | --- |
| KEYWORD_CORE | int | KW_INT | KEYWORD_INT |  Aceita | Corresponde exatamente a uma das palavras reservadas |
| KEYWORD_CORE | intx | REJECTED | REJECTED | Rejeitada / Interação | o 'x' faz com que ele não seja uma palavra reservada e por ele, a palavra se torna um identificador comum |
| KEYWORD_CORE | print | KW_PRINT | KEYWORD_PRINT | Aceita | Corresponde exatamente a uma das palavras reservadas |
| KEYWORD_CORE | "" | REJECTED | REJECTED | Fronteira |A string vazia não corresponde a nenhuma das palavras reservadas |

## KEYWORD_EXT
### Classe e finalidade
Palavras reservadas na parte de extensão (palavras a mais)

### Descrição informal
Representa as palavras-chave adicionadas à linguagem para suportar estruturas de controle (condicionais e laços de repetição)

### Exemplos aceitos
"if", "else", "while"

### Definição matemática
$RExt = \{\text{"if"}, \text{"else"}, \text{"while"}\}$

### Conjuntos auxiliares
Não tem

### Expressão regular formal
$rExt = \text{"if"} \cup \text{"else"} \cup \text{"while"}$

### Regex de Python
```python
r"if|else|while"
```

### Ação futura do lexer
Reconhece a palavra e emiti o token que corresponde ao que esta reservado na extenção (ex: KW_IF, KW_ELSE, ou KW_WHILE)

### Testes e interações

| Classe | Entrada | Esperado | Obtido | Categoria | Justificativa |
| --- | --- | --- | --- | --- | --- |
| KEYWORD_EXT | if | KW_IF | KEYWORD_IF | Aceita | Corresponde exatamente à palavra reservada |
| KEYWORD_EXT | while | KW_WHILE | KEYWORD_WHILE | Aceita | Corresponde exatamente à palavra reservada |
| KEYWORD_EXT | while1 | REJECTED | REJECTED | Rejeitada/Interação | O dígito no final invalida a correspondência exata e a transforma em identificador |
| KEYWORD_EXT | else | KW_ELSE | KEYWORD_ELSE | Aceita | Corresponde exatamente à palavra reservada |

