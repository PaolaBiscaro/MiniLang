import re

WHITESPACES = re.compile(r'[ \t\r\n]+')

def identify_and_ignores_whitespace(word: str) -> str:
    list_words = WHITESPACES.split(word)
    result = []
    i = 0
    
    for words in list_words:
        if words != '':
            result.append(words)
    
    return result


#Casos de teste
word = "int valor"
word2 = "\nint valor = 1 + 1 "
word3 = "\n \t int valor2 = 2 + 2 \n"
word4 = ''
word5 = "\n"
word6 = "\n \t"
word7 = " 1 + 1"


print(identify_and_ignores_whitespace(word7))

#Um compilador nao envia ao parse o token WHITESPACE, ele remove e envia somente o necessario