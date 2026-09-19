SINGLE_CHAR_TOKENS = {
    '/': "SLASH",
    '+': "PLUS",
    '-': "MINUS",
    '*': "STAR",
    '(': "LPAREN",
    ')': "RPAREN",
    '{': "LBRACE",
    '}': "RBRACE",
    ';': "SEMICOLON",
}

KEYWORDS = {
    "int": "KW_INT",
    "print": "KW_PRINT",
    "if": "KW_IF",
    "else": "KW_ELSE",
    "while": "KW_WHILE",
}

#Indices
start = 0
start_line = 1
start_column = 1

source = ""
current = 0
line = 1
column = 1

tokens = []
errors = []

def scan_tokens():
    global start, start_line, start_column

    while not at_end():
        start = current
        start_line = line
        start_column = column
        scan_token()

    tokens.append({
        "type": "EOF",
        "lexeme": "",
        "line": line,
        "column": column,
    })
    return tokens, errors
        
def scan_token():
    if peek() == "/" and peek_next() == "/":
        advance()
        advance()
        line_comment()
        return
    
    c = advance()
    
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or (c == '_'):
        identifier()
    
    elif '0' <= c <= '9':
        number()
        
    elif c == "/":
        add_token("SLASH")
    
    elif c == "=":
        if match("="):
            add_token("EQUAL_EQUAL")
            
        else:
            add_token("ASSIGN")
    
    elif c == "!":
        if match("="):
            add_token("BANG_EQUAL")
        else:
            report_invalid_character(c)
    
    elif c == "<":
        if match("="):
            add_token("LESS_EQUAL")
        else:
            add_token("LESS")
            
    elif c == ">":
            if match("="):
                add_token("GREATER_EQUAL")
            else:
                add_token("GREATER")
    
    elif c in SINGLE_CHAR_TOKENS:
        token_type = SINGLE_CHAR_TOKENS[c]
        add_token(token_type, c)
        
    elif c in (' ', '\t', '\r', '\n'):
        while peek() in (' ', '\t', '\r', '\n'):
            advance()
    else:
        report_invalid_character(c)
        
        
        
    
def at_end():
    return current >= len(source)
    

def advance():
    global current, line, column

    char = source[current]
    current += 1

    if char in ('\r', '\n'):
        line += 1
        column = 1
    else:
        column += 1

    return char    

def peek():
    if at_end():
        return '\0'
    return source[current]

def peek_next():
    if current + 1 >= len(source):
        return '\0'

    return source[current + 1]

def match(expected):
    if at_end():
        return False
    
    if source[current] == expected:
        advance()
        return True
    
    return False

def add_token(token_type, lexeme=None):
    if lexeme is None:
        lexeme = source[start:current]

    token = {
        "type": token_type,
        "lexeme": lexeme,
        "line": start_line,
        "column": start_column,
    }

    tokens.append(token)

def identifier():  # depende de source, start, current, peek, advance e add_token
    while (
        ('a' <= peek() <= 'z')
        or ('A' <= peek() <= 'Z')
        or ('0' <= peek() <= '9')
        or peek() == '_'
    ):
        advance()

    lexeme = source[start:current]

    if lexeme in KEYWORDS:
        add_token(KEYWORDS[lexeme])
    else:
        add_token("IDENT")

def number():
    while not at_end():
        if peek() >= '0' and peek() <= '9':
            advance()
        else:
            break
    add_token("INT_LITERAL")

def line_comment():
    while not at_end() and peek() not in ('\r', '\n'):
        advance()

def report_invalid_character(c):
    error = {
        "character": c,
        "line": start_line,
        "column": start_column,
        "message": "Caractere inválido",
    }

    errors.append(error)

        