from reconhecedores.rArith import rArith
from reconhecedores.rAssign import rAssing
from reconhecedores.comparison import rel_op
from reconhecedores.delimiter import classify_delimiter
from reconhecedores.identifiers import classify_ident
from reconhecedores.intLiteral import classify_int_literal
from reconhecedores.line_comment import identify_and_ignores_line_comment
from reconhecedores.whitespace import identify_and_ignore_whitespace


lista_testes_arith = ["+", "-", "*", "/", "a", "1", "//", "**", "", "++", "//x", "-10", "+7"]
lista_testes_assign = ["=", "a", "1", "==", "===", ""]
lista_testes_rel_op = ["<", ">", "<=", ">=", "==", "!=", "a", "1", "!", "=>", "===", "", "="]
lista_testes_delimiter = ["(", ")", ";", "{", "}", ",", "a", "1", "()", "{}", ");", ""]
lista_testes_ident = ["var", "var1", "_contador", "total_2", "int", "print", "if", "else", "while", "intx", "print2", "ifx", "else2", "while1", "1var", "var$", "a b", "ação", "_", "", "valor", "x", "y", "int \tvalor=1;", "int// comentário\nvalor;", "x// comentário\ry", "x// comentário\r\ny", "print(1); // fim", " \t// só comentário\r\n"]
lista_testes_int_literal = ["123", "0", "001", "42", "a123", "12a", "-10", "+7", "1.5", "", "1", "10", "7", "+", "-"]
lista_testes_line_comment = ["// This is a comment", "//x", "////", "// + - * / = <> {} () ;", "This is not a comment", "/* comentario */", "//x\n", "//x\r", "//", "/", "", "// comentário", "// fim", "// só comentário", "int \tvalor=1;", "int// comentário\nvalor;", "x// comentário\ry", "x// comentário\r\ny", "print(1); // fim", " \t// só comentário\r\n"]
lista_testes_whitespace = [" ", "\t", "\n", "\r", " \t\r\n", "a", "1", " a", "a b", "\v", "\f", "", " \t", "\r\n", "int \tvalor=1;", "int// comentário\nvalor;", "x// comentário\ry", "x// comentário\r\ny", "print(1); // fim", " \t// só comentário\r\n"]


def testar_lista(palavras, reconhecedor):
    return {palavra: reconhecedor(palavra) for palavra in palavras}

def test_rArith(palavras):
    return testar_lista(palavras, rArith)

def test_rAssign(palavras):
    return testar_lista(palavras, rAssing)

def test_rel_op(palavras):
    return testar_lista(palavras, rel_op)

def test_classify_delimiter(palavras):
    return testar_lista(palavras, classify_delimiter)

def test_classify_ident(palavras):
    return testar_lista(palavras, classify_ident)

def test_classify_int_literal(palavras):
    return testar_lista(palavras, classify_int_literal)

def test_identify_and_ignores_line_comment(palavras):
    return testar_lista(palavras, identify_and_ignores_line_comment)

def test_identify_and_ignore_whitespace(palavras):
    return testar_lista(palavras, identify_and_ignore_whitespace)

def main():
    print("ARITH_OP:")
    print(test_rArith(lista_testes_arith))
    print("\nASSIGN:")
    print(test_rAssign(lista_testes_assign))
    print("\nREL_OP:")
    print(test_rel_op(lista_testes_rel_op))
    print("\nDELIMITER_CORE / BLOCK_DELIMITER:")
    print(test_classify_delimiter(lista_testes_delimiter))
    print("\nIDENT_BASE / KEYWORD_CORE / KEYWORD_EXT:")
    print(test_classify_ident(lista_testes_ident))
    print("\nINT_LITERAL:")
    print(test_classify_int_literal(lista_testes_int_literal))
    print("\nLINE_COMMENT:")
    print(test_identify_and_ignores_line_comment(lista_testes_line_comment))
    print("\nWHITESPACE:")
    print(test_identify_and_ignore_whitespace(lista_testes_whitespace))


if __name__ == "__main__":
    main()
