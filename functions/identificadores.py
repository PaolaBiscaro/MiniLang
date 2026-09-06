import re

IDENT_BASE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")

KEYWORD_CORE = {"int","print"}
KEYWORD_EXT = {"if","else","while"}

def classify_ident(word : str) -> str:
    if IDENT_BASE.fullmatch(word) is not None:
        if word in KEYWORD_CORE or word in KEYWORD_EXT:
            return f"KEYWORD_{word.upper()}"
        else:
            return "IDENT"

    return "REJECTED"

#testeziho de cada classificação
print(classify_ident("total2"))   
print(classify_ident("2valor"))
print(classify_ident("_contador"))
print(classify_ident("x"))
print(classify_ident(""))
print(classify_ident("total-2"))

print(classify_ident("int"))
print(classify_ident("intx"))
print(classify_ident("print"))
print(classify_ident("print2"))
print(classify_ident("if"))
print(classify_ident("else"))
print(classify_ident("while1")) 
print(classify_ident("while"))