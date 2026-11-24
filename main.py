from pathlib import Path
import sys

from minilang import ast_nodes, lexer, parser, semantic


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    caminho = Path(__file__).parent / "arquivo-txt" / "programa.txt"

    try:
        texto = caminho.read_text(encoding="utf-8")
    except OSError as erro:
        print(f"Erro ao ler {caminho}: {erro}")
        return 1

    lexer.source = texto.replace("\r\n", "\n")
    lexer.start = 0
    lexer.current = 0
    lexer.line = 1
    lexer.column = 1
    lexer.start_line = 1
    lexer.start_column = 1
    lexer.tokens = []
    lexer.errors = []

    tokens, errors = lexer.scan_tokens()

    if errors:
        error = errors[0]
        print(
            f'Erro léxico na linha {error["line"]}, '
            f'coluna {error["column"]}: '
            f'{error["message"]}: {error["character"]!r}.'
        )
        return 1

    parser.iniciar(tokens)

    try:
        arvore = parser.programa()
    except SyntaxError as erro:
        print(f"Erro sintático: {erro}")
        return 1

    escopos, diagnosticos = semantic.analisar(arvore)

    print("Tabelas de símbolos")
    for escopo, tabela in enumerate(escopos):
        nome_escopo = "global" if escopo == 0 else "bloco"
        print(f"Escopo {escopo} ({nome_escopo})")
        if not tabela:
            print("  (sem declarações)")
        for nome, simbolo in tabela.items():
            token = simbolo["token"]
            print(
                f'  {simbolo["id"]} {nome}: {simbolo["tipo"]} '
                f'em {token["line"]}:{token["column"]}'
            )

    print("\nAST anotada")
    print(ast_nodes.visualizar(arvore))

    print("\nDiagnósticos semânticos")
    if not diagnosticos:
        print("Nenhum erro semântico.")
    for erro in diagnosticos:
        print(
            f'{erro["linha"]}:{erro["coluna"]} '
            f'[{erro["codigo"]}] {erro["mensagem"]}'
        )

    return 1 if diagnosticos else 0


if __name__ == "__main__":
    raise SystemExit(main())
