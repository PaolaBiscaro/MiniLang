import re

LINE_COMMENT = re.compile(r"//[^\r\n]*")

def identify_and_ignores_line_comment(word : str) -> str:
    
    result = LINE_COMMENT.sub("", word)
    return result
    #return repr(result) #Caso precise enxergar os \n
    
#Casos de teste
word = "//\n \n \n \n // oi \n int valor; //\n"
word2 = "//"
word3 = "\n int teste"
word4 = "int //este e um comentario sem a quebra de linha..."
word5 = "//comentario \n \n int 10"
word6 = "// // outro comentario \n  teste"
word7 = "// //"


print(identify_and_ignores_line_comment(word6))

#Um compilador nao envia ao parse o token LINE_COMMENT, ele remove esse token.