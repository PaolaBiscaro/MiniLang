import re
def rArith(value : str):
  if (re.fullmatch(r"[+*/-]", value)):
    return "Arith"
  return None