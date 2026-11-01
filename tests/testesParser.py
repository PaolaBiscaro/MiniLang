from pathlib import Path
import sys

PASTA_PROJETO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PASTA_PROJETO))

from minilang import lexer, parser


def analisar(texto):
    # Reinicia o estado global do lexer.
    lexer.source = texto
    lexer.start = 0
    lexer.current = 0
    lexer.line = 1
    lexer.column = 1
    lexer.start_line = 1
    lexer.start_column = 1
    lexer.tokens = []
    lexer.errors = []

    tokens, erros = lexer.scan_tokens()
    assert erros == [], f"Erros léxicos inesperados: {erros}"

    parser.iniciar(tokens)
    arvore = parser.programa()

    assert parser.peek()["type"] == "EOF"
    return arvore


def test_declaracao_atribuicao_print():
    arvore = analisar("int x; x = 2; print(x);")
    comandos = arvore["comandos"]

    assert arvore["tipo"] == "Programa"
    assert len(comandos) == 3
    assert comandos[0]["tipo"] == "Declaracao"
    assert comandos[1]["tipo"] == "Atribuicao"
    assert comandos[2]["tipo"] == "Saida"

    # "int x" - [FALHOU]
    # "int $x;" - [FALHOU] - Erro lexico


def test_precedencia():
    casos = [
        # Cada caso: código, operador da raiz, lado esperado, operador nesse lado.
        ("print(2 + 3 * 4);", "+", "direita", "*"),
        ("print(2 - 3 / 4);", "-", "direita", "/"),
        ("print(2 * 3 / 4);", "/", "esquerda", "*"),
        ("print(2 * 3 + 4);", "+", "esquerda", "*"),
        ("print(2 + 3 - 4);", "-", "esquerda", "+"),
    ]

    for codigo, raiz_esperada, lado, operador_esperado in casos:
        arvore = analisar(codigo)
        expressao = arvore["comandos"][0]["expressao"]

        assert expressao["operador"]["lexeme"] == raiz_esperada
        assert expressao[lado]["operador"]["lexeme"] == operador_esperado

    # "print(2 + * 4);" - [FALHOU] 
    # "print(2 / );" - [FALHOU]


def test_parenteses():
    arvore = analisar("print((2 + 3) * 4);")
    produto = arvore["comandos"][0]["expressao"]

    assert produto["operador"]["lexeme"] == "*"
    assert produto["esquerda"]["operador"]["lexeme"] == "+"

    # "print((2 + 3) * 4;" - [FALHOU]
    # "print(());" - [FALHOU]


def test_associatividade_a_esquerda():
    arvore = analisar("print(10 + 3 - 2);")
    subtracao = arvore["comandos"][0]["expressao"]

    assert subtracao["operador"]["lexeme"] == "-"
    assert subtracao["esquerda"]["tipo"] == "Binaria"
    assert subtracao["esquerda"]["operador"]["lexeme"] == "+"

    # "print(10 + 3 -);" - [FALHOU]
    # "print(10 + -2);" - [FALHOU]


def test_sequencia_de_comandos():
    arvore = analisar("int x; x = 2 + 3; print(x);")
    tipos = [comando["tipo"] for comando in arvore["comandos"]]

    assert tipos == ["Declaracao", "Atribuicao", "Saida"]

    # "int x;;" - [FALHOU]
    # "int x; print(x)" - [FALHOU]


def test_programa_vazio():
    arvore = analisar("")

    assert arvore == {
        "tipo": "Programa",
        "comandos": [],
    }

    # "   "  - [OK]  
    # "// comentário" - [OK]
    # "print(1);" - [FALHOU]


def test_variavel_nao_declarada_e_valida_sintaticamente():
    arvore = analisar("print(y);")

    assert arvore["comandos"][0]["tipo"] == "Saida"
    assert arvore["comandos"][0]["expressao"]["token"]["lexeme"] == "y"

    # "print(y);" - [OK] 
    # "print(y + );" - [FALHOU] 
    # "print(y;" - [FALHOU]


def test_entradas_invalidas():
    entradas = [
        "print(2 + );",
        "int x",
        "x = 2 + 3",
        "print(2 + 3;",
        "print()",
        "x = ;"
    ]

   

    for texto in entradas:
        lexer.source = texto
        lexer.start = 0
        lexer.current = 0
        lexer.line = 1
        lexer.column = 1
        lexer.start_line = 1
        lexer.start_column = 1
        lexer.tokens = []
        lexer.errors = []

        tokens, erros = lexer.scan_tokens()
        assert erros == []

        parser.iniciar(tokens)

        try:
            parser.programa()
            assert False, f"Era esperado erro sintático para: {texto}"
        except SyntaxError as erro:
            mensagem = str(erro)
            assert "Linha" in mensagem
            assert "coluna" in mensagem
            assert "esperado" in mensagem
            assert "encontrado" in mensagem


def executar_teste(nome, funcao):
    try:
        funcao()
        print(f"[OK] {nome}")
        return True
    except Exception as erro:
        print(f"[FALHOU] {nome}: {erro}")
        return False


def main():
    testes = [
        ("declaração, atribuição e print", test_declaracao_atribuicao_print),
        ("precedência", test_precedencia),
        ("parênteses", test_parenteses),
        ("associatividade à esquerda", test_associatividade_a_esquerda),
        ("sequência de comandos", test_sequencia_de_comandos),
        ("programa vazio", test_programa_vazio),
        (
            "variável não declarada, mas válida sintaticamente",
            test_variavel_nao_declarada_e_valida_sintaticamente,
        ),
        ("entradas inválidas", test_entradas_invalidas),
    ]

    aprovados = 0

    for nome, funcao in testes:
        if executar_teste(nome, funcao):
            aprovados += 1

    print(f"\nResultado: {aprovados}/{len(testes)} testes aprovados.")


if __name__ == "__main__":
    main()