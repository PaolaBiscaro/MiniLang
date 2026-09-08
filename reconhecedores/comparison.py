import re

def rel_op(value : str):
    tokens = {
        "<": "LESS_THAN",
        ">": "GREATER_THAN",
        "<=": "LESS_THAN_EQUAL",
        ">=": "GREATER_THAN_EQUAL",
        "==": "EQUAL",
        "!=": "NOT_EQUAL"
    }
    if (re.fullmatch(r"[<>]=?|==|!=", value)):
        return tokens.get(value)
    return None
