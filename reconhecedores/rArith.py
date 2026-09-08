import re
def rArith(value : str):
  tokens = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH"
  } 

  if (re.fullmatch(r"[+*/-]", value)):
    return tokens.get(value)
  return None

if __name__ == "__main__":
  word = rArith("/")
  print(word)
