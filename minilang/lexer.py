"""
scan_tokens - Paola
scan_token - Paola
at_end - Heloisa
advance - Lorena
peek - Lucas
peek_next - Heloisa
match - Lorena
add_token - Lucas
identifier - Heloisa
number - Lorena
line_comment - Paola
report_invalid_character - Lucas
"""

import re

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

def scan_tokens():
    while not at_end():
        
        """start ← current
            start_line ← line
            start_column ← column"""
            
        scan_token()
        
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
    pass

def peek():
    pass

def peek_next():
    if current + 1 >= len(source):
        return '\0'

    return source[current + 1]

def match():
    pass

def add_token():
    pass

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
    pass

def line_comment():
    while not at_end() and peek() not in ('\r', '\n'):
        advance()

def report_invalid_character():
    pass 

        