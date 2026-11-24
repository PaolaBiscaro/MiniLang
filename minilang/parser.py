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

    if match(["TRUE", "FALSE"]):
        return ast_nodes.booleano(previous())

    if match(["IDENT"]):
        token = previous()
        return ast_nodes.identificador(token)

    if match(["LPAREN"]):
        no = expressao()
        expect("RPAREN")
        return no

    raise erro_sintatico('inteiro, booleano, identificador ou "("')


def termo():
    esquerda = factor()

    while match(["STAR", "SLASH"]):
        operador = previous()
        direita = factor()

        esquerda = ast_nodes.binaria(esquerda, operador, direita)

    return esquerda


def expressao_aritmetica():
    esquerda = termo()

    while match(["PLUS", "MINUS"]):
        operador = previous()
        direita = termo()

        esquerda = ast_nodes.binaria(esquerda, operador, direita)

    return esquerda


def expressao():
    esquerda = expressao_aritmetica()

    if match([
        "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL",
        "EQUAL_EQUAL", "BANG_EQUAL",
    ]):
        operador = previous()
        direita = expressao_aritmetica()
        return ast_nodes.binaria(esquerda, operador, direita)

    return esquerda


def atribuicao():
    identificador = expect("IDENT")
    expect("ASSIGN")
    expressao_atribuida = expressao()
    expect("SEMICOLON")

    return ast_nodes.atribuicao(identificador, expressao_atribuida)

def declaracao(tipo):
    tipo_token = expect(tipo)
    identificador = expect("IDENT")
    expect("SEMICOLON")

    return ast_nodes.declaracao(identificador, tipo_token)

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
        return declaracao("KW_INT")

    if token["type"] == "KW_BOOL":
        return declaracao("KW_BOOL")

    if token["type"] == "IDENT":
        return atribuicao()

    if token["type"] == "KW_PRINT":
        return saida()

    if token["type"] == "KW_IF":
        return comando_if()

    if token["type"] == "KW_WHILE":
        return comando_while()

    if token["type"] == "KW_FOR":
        return comando_for()
    if token["type"] == "LBRACE":
        return bloco()

    raise erro_sintatico(
        "declaração, atribuição, print, if, while ou for", token
    )
    
    
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


def bloco():
    expect("LBRACE")
    comandos = []

    while not at_end() and peek()["type"] != "RBRACE":
        comandos.append(item())

    expect("RBRACE")
    return ast_nodes.bloco(comandos)


def comando_if():
    token = expect("KW_IF")
    expect("LPAREN")
    teste = expressao()
    expect("RPAREN")
    entao = bloco()
    senao = None

    if match(["KW_ELSE"]):
        senao = bloco()

    return ast_nodes.se(token, teste, entao, senao)


def comando_while():
    token = expect("KW_WHILE")
    expect("LPAREN")
    teste = expressao()
    expect("RPAREN")
    corpo = bloco()
    return ast_nodes.enquanto(token, teste, corpo)


def atribuicao_sem_ponto_virgula():
    identificador = expect("IDENT")
    expect("ASSIGN")
    valor = expressao()
    return ast_nodes.atribuicao(identificador, valor)


def comando_for():
    token = expect("KW_FOR")
    expect("LPAREN")

    inicializacao = atribuicao_sem_ponto_virgula()
    expect("SEMICOLON")

    teste = expressao()
    expect("SEMICOLON")

    atualizacao = atribuicao_sem_ponto_virgula()
    expect("RPAREN")

    corpo = bloco()
    return ast_nodes.para(token, inicializacao, teste, atualizacao, corpo)
