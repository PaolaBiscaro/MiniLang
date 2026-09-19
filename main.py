from pathlib import Path
from minilang import lexer


def main():
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

    print("TOKENS")
    for token in tokens:
        print(
            f'{token["line"]}:{token["column"]} '
            f'{token["type"]} {token["lexeme"]!r}'
        )

    print("\nDIAGNÓSTICOS")
    for error in errors:
        print(
            f'{error["line"]}:{error["column"]} '
            f'{error["message"]}: {error["character"]!r}'
        )

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())