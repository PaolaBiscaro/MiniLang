from pathlib import Path
import sys

from minilang import ast_nodes, lexer, parser


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

    print(ast_nodes.visualizar(arvore))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
