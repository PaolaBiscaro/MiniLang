import re

def classify_delimiter(word:str) -> str:
    DELIMITER_CORE = re.compile(r"[();]")
    BLOCK_DELIMITER = re.compile(r"[{}]")
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
   
    return None
        
