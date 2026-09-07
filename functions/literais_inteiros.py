import re

def literais_inteiros(value : str):
    if (re.fullmatch(r"[0-9]+", value)):
        return "Literal Inteiro"
    return None
