import re 

def rAssing(value : str):
  if (re.fullmatch(r"[=]", value)):
    return "ASSIGN"

  return None
