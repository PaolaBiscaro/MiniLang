import re 

def rAssing(value : str):
  if (re.fullmatch(r"[=]", value)):
    return "Assign"

  return None

valor = rAssing("+")
print(valor)