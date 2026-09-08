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
        

if __name__ == "__main__":
    # Exemplos de palavras candidatas a um único delimitador.
    word = " "
    word2 = ";;;"
    word3 = "valor;;"
    word4 = "("
    word5 = ")"
    word6 = "}"
    word7 = ";"

    print(classify_delimiter(word))
