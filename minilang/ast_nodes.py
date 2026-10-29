#esses são os nós que vamos usar para montar a arvore 
def inteiro(token):
    return {
        "tipo": "Inteiro",
        "token": token,
    }


def identificador(token):
    return {
        "tipo": "Identificador",
        "token": token,
    }


def binaria(esquerda, operador, direita):
    return {
        "tipo": "Binaria",
        "esquerda": esquerda,
        "operador": operador,
        "direita": direita,
    }


def declaracao(identificador):
    return {
        "tipo": "Declaracao",
        "identificador": identificador,
    }


def atribuicao(identificador, expressao):
    return {
        "tipo": "Atribuicao",
        "identificador": identificador,
        "expressao": expressao,
    }


def saida(expressao):
    return {
        "tipo": "Saida",
        "expressao": expressao,
    }


def programa(comandos):
    return {
        "tipo": "Programa",
        "comandos": comandos,
    }


def _rotulo(no): #usado no visualizar
    tipo = no["tipo"]

    if tipo == "Inteiro":
        return f'{tipo}({no["token"]["lexeme"]})'

    if tipo == "Identificador":
        return f'Variavel({no["token"]["lexeme"]})'

    if tipo == "Binaria":
        return f'Binaria({no["operador"]["lexeme"]})'

    if tipo in ("Declaracao", "Atribuicao"):
        return f'{tipo}({no["identificador"]["lexeme"]})'

    return tipo


def _filhos(no):#usado no visualizar
    tipo = no["tipo"]

    if tipo == "Programa":
        return no["comandos"]

    if tipo == "Binaria":
        return [no["esquerda"], no["direita"]]

    if tipo in ("Atribuicao", "Saida"):
        return [no["expressao"]]

    return []


def visualizar(no): #para fazer o arvore bonitinha no terminal
    linhas = []

    def visitar(atual, prefixo="", ultimo=True, raiz=False):
        conector = "" if raiz else ("└── " if ultimo else "├── ")
        linhas.append(f"{prefixo}{conector}{_rotulo(atual)}")

        filhos = _filhos(atual)
        prefixo_filho = prefixo if raiz else prefixo + ("    " if ultimo else "│   ")

        for indice, filho in enumerate(filhos):
            visitar(
                filho,
                prefixo_filho,
                ultimo=indice == len(filhos) - 1,
            )

    visitar(no, raiz=True)
    return "\n".join(linhas)
