import re

def classify_ident(word : str) -> str:
    IDENT_BASE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")

    KEYWORD_CORE = {"int","print"}
    KEYWORD_EXT = {"if","else","while"}
    if IDENT_BASE.fullmatch(word) is not None:
        if word in KEYWORD_CORE or word in KEYWORD_EXT:
            return f"KEYWORD_{word.upper()}"
        else:
            return "IDENT"

    return "REJECTED"
