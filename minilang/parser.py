from minilang import ast_nodes

tokens = []
current = 0


def iniciar(lista_tokens):
    global tokens, current

    if not lista_tokens:
        return ValueError("A lista de tokens não pode ser vazia.")

    tokens = lista_tokens
    current = 0


def peek():
    return tokens[current]


def at_end():
    return peek()["type"] == "EOF"


def advance():
    global current

    token = peek()

    if not at_end():
        current += 1

    return token


def previous():
    if current >= 1:
        return tokens[current - 1]


def match(tipos):
    if peek()["type"] in tipos:
        advance()
        return True

    return False


def erro_sintatico(esperado, token=None): #Ela informa o que o parser esperava, qual token encontrou e sua posição
    if token is None:
        token = peek()

    linha = token.get("line", "?")
    coluna = token.get("column", "?")
    tipo = token.get("type", "DESCONHECIDO")
    lexema = token.get("lexeme", "")

    return SyntaxError(
        f"Linha {linha}, coluna {coluna}: "
        f"esperado {esperado}, encontrado {tipo} ({lexema!r})."
    )


def expect(tipo):
    token = peek()

    if token["type"] == tipo:
        return advance()

    raise erro_sintatico(tipo, token)

def factor():
    if match(["INT_LITERAL"]):
        token = previous()
        return ast_nodes.inteiro(token)

    if match(["IDENT"]):
        token = previous()
        return ast_nodes.identificador(token)

    if match(["LPAREN"]):
        no = expressao()
        expect("RPAREN")
        return no

    raise erro_sintatico('inteiro, identificador ou "("')


def termo():
    esquerda = factor()

    while match(["STAR", "SLASH"]):
        operador = previous()
        direita = factor()

        esquerda = ast_nodes.binaria(
            esquerda,
            operador,
            direita,
        )

    return esquerda


def expressao():
    esquerda = termo()

    while match(["PLUS", "MINUS"]):
        operador = previous()
        direita = termo()

        esquerda = ast_nodes.binaria(
            esquerda,
            operador,
            direita,
        )

    return esquerda

def atribuicao():
    identificador = expect("IDENT")
    expect("ASSIGN")
    expressao_atribuida = expressao()
    expect("SEMICOLON")

    return ast_nodes.atribuicao(identificador, expressao_atribuida)

def declaracao():
    expect("KW_INT")
    identificador = expect("IDENT")
    expect("SEMICOLON")

    return ast_nodes.declaracao(identificador)

def saida():
    expect("KW_PRINT")
    expect("LPAREN")
    expressao_saida = expressao()
    expect("RPAREN")
    expect("SEMICOLON")

    return ast_nodes.saida(expressao_saida)

def item():
    token = peek()

    if token["type"] == "KW_INT":
        return declaracao()

    if token["type"] == "IDENT":
        return atribuicao()

    if token["type"] == "KW_PRINT":
        return saida()

    raise erro_sintatico("declaração, atribuição ou print", token)
    
def lista_itens():
    comandos = []

    while not at_end():
        comando = item()
        comandos.append(comando)

    return comandos


def programa():
    comandos = lista_itens()

    expect("EOF")

    return ast_nodes.programa(comandos)
