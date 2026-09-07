import re

DELIMITER_CORE = re.compile(r"[();]")
BLOCK_DELIMITER = re.compile(r"[{}]")

def classify_delimiter(word:str) -> str:
    tokens = {
        "(": "LPAREN",
        ")": "RPAREN",
        "{": "LCHAVE",
        "}": "RCHAVE",
        ";": "SEMICOLON",
    }
    
    
    if DELIMITER_CORE.fullmatch(word) is not None:
        result = tokens.get(word)
        return result
    
    if BLOCK_DELIMITER.fullmatch(word) is not None:
        result = tokens.get(word)
        return result
   
    return "REJECTED"
        

#Casos de teste
word = "valor;" #??
word2 = ";;;"
word3 = "valor;;"
word4 = "("
word5 = ")"
word6= "}"
word7 = ";"

print(classify_delimiter(word))