import re

def classify_int_literal(value : str):
    if (re.fullmatch(r"[0-9]+", value)):
        return "INT_LITERAL"
    return None
