#esses são os nós que vamos usar para montar a arvore 
def inteiro(token):
    return {
        "tipo": "Inteiro",
        "token": token,
        "tipo_expr": "int",
    }


def booleano(token):
    return {"tipo": "Booleano", "token": token, "tipo_expr": "bool"}


def identificador(token):
    return {
        "tipo": "Identificador",
        "token": token,
        # O tipo depende da declaração visível neste ponto do programa.
        # Ele será preenchido pela análise semântica.
        "tipo_expr": None,
    }


def binaria(esquerda, operador, direita, tipo_expr=None):
    return {
        "tipo": "Binaria",
        "esquerda": esquerda,
        "operador": operador,
        "direita": direita,
        "tipo_expr": tipo_expr,
    }


def declaracao(identificador, tipo_token=None):
    return {
        "tipo": "Declaracao",
        "identificador": identificador,
        "tipo_token": tipo_token,
        "tipo_declarado": tipo_token["lexeme"] if tipo_token else None,
    }


def atribuicao(identificador, expressao):
    return {
        "tipo": "Atribuicao",
        "identificador": identificador,
        "expressao": expressao,
    }
    
def bloco(comandos):
    return {"tipo": "Bloco", "comandos": comandos}


#if
def se(token, condicao, entao, senao=None):
    return {
        "tipo": "Se",
        "token": token,
        "condicao": condicao,
        "entao": entao,
        "senao": senao,
    }

#while
def enquanto(token, condicao, corpo):
    return {"tipo": "Enquanto", "token": token, "condicao": condicao, "corpo": corpo}


#for
def para(token, inicializacao, condicao, atualizacao, corpo):
    return {
        "tipo": "Para",
        "token": token,
        "inicializacao": inicializacao,
        "condicao": condicao,
        "atualizacao": atualizacao,
        "corpo": corpo,
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
    simbolo = no.get("simbolo")
    vinculo = ""
    if simbolo is not None:
        vinculo = f' -> {simbolo["id"]}'
    elif "simbolo" in no:
        vinculo = " -> sem vínculo"

    if tipo in ("Inteiro", "Booleano"):
        return f'{tipo}({no["token"]["lexeme"]}):{no["tipo_expr"]}'

    if tipo == "Identificador":
        tipo_expr = no.get("tipo_expr") or "?"
        return f'Variavel({no["token"]["lexeme"]}):{tipo_expr}{vinculo}'

    if tipo == "Binaria":
        tipo_expr = no.get("tipo_expr") or "?"
        return f'Binaria({no["operador"]["lexeme"]}):{tipo_expr}'

    if tipo == "Declaracao":
        tipo_declarado = no.get("tipo_declarado") or "?"
        return f'Declaracao({no["identificador"]["lexeme"]}):{tipo_declarado}{vinculo}'

    if tipo == "Atribuicao":
        return f'{tipo}({no["identificador"]["lexeme"]}){vinculo}'

    if tipo == "Bloco" and "escopo" in no:
        return f'Bloco (escopo {no["escopo"]})'

    return tipo


def _filhos(no):
    tipo = no["tipo"]

    if tipo in ("Programa", "Bloco"):
        return no["comandos"]

    if tipo == "Binaria":
        return [no["esquerda"], no["direita"]]

    if tipo in ("Atribuicao", "Saida"):
        return [no["expressao"]]

    if tipo == "Se":
        filhos = [no["condicao"], no["entao"]]
        if no["senao"] is not None:
            filhos.append(no["senao"])
        return filhos

    if tipo == "Enquanto":
        return [no["condicao"], no["corpo"]]

    if tipo == "Para":
        return [
            no["inicializacao"],
            no["condicao"],
            no["atualizacao"],
            no["corpo"],
        ]

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
