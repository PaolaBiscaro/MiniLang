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