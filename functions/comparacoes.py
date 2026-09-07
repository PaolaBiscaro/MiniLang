import re

def rel_op(value : str):
    if (re.fullmatch(r"[<>]=?|==|!=", value)):
        return "Operador Relacional"
    return None
