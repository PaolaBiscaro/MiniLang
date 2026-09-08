import re

def identify_and_ignores_line_comment(word: str) -> bool:
    LINE_COMMENT = re.compile(r"//[^\r\n]*")
    return LINE_COMMENT.fullmatch(word) is not None


if __name__ == "__main__":
    # Exemplos: quebras de linha e outros lexemas não pertencem ao comentário.
    word = "//\n \n \n \n // oi \n int valor; //\n"
    word2 = "//"
    word3 = "\n int teste"
    word4 = "int //este e um comentario sem a quebra de linha..."
    word5 = "//comentario \n \n int 10"
    word6 = "// // outro comentario \n  teste"
    word7 = "// //"

    print(identify_and_ignores_line_comment(word6))

    # O lexer futuro ignorará os comentários reconhecidos; esta função só reconhece.
