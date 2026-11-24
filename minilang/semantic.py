ERRO = "ERRO"


def analisar(arvore):
    escopos = [{}]
    ativos = [0]
    diagnosticos = []
    proximo_simbolo = 0

    def diagnosticar(codigo, token, mensagem):
        diagnosticos.append({
            "codigo": codigo,
            "linha": token["line"],
            "coluna": token["column"],
            "mensagem": mensagem,
        })

    def declarar(no):
        nonlocal proximo_simbolo

        token = no["identificador"]
        nome = token["lexeme"]
        tabela = escopos[ativos[-1]]
        if nome in tabela:
            anterior = tabela[nome]["token"]
            diagnosticar(
                "E_REDECLARACAO", token,
                f'{nome!r} já foi declarado neste escopo na linha '
                f'{anterior["line"]}, coluna {anterior["column"]}.',
            )
            no["simbolo"] = None
            return

        simbolo = {
            "id": f"s{proximo_simbolo}",
            "tipo": no["tipo_declarado"],
            "token": token,
        }
        proximo_simbolo += 1
        tabela[nome] = simbolo
        no["simbolo"] = simbolo

    def resolver(token):
        nome = token["lexeme"]
        for escopo in reversed(ativos):
            tabela = escopos[escopo]
            if nome in tabela:
                return tabela[nome]

        diagnosticar(
            "E_NOME", token, f"Identificador {nome!r} não declarado neste ponto."
        )
        return None

    def tipar_binaria(no):
        esquerda = tipar(no["esquerda"])
        direita = tipar(no["direita"])
        if ERRO in (esquerda, direita):
            return ERRO

        token = no["operador"]
        operador = token["lexeme"]
        if operador in ("==", "!="):
            permitido = esquerda == direita
            esperado = "dois operandos do mesmo tipo (int ou bool)"
            resultado = "bool"
        else:
            permitido = esquerda == direita == "int"
            esperado = "dois operandos do tipo int"
            resultado = "int" if operador in ("+", "-", "*", "/") else "bool"

        if permitido:
            return resultado

        diagnosticar(
            "E_TIPO", token,
            f"Operador {operador!r} exige {esperado}, recebeu {esquerda} e {direita}.",
        )
        return ERRO

    def tipar(no):
        if no["tipo"] == "Identificador":
            simbolo = resolver(no["token"])
            no["simbolo"] = simbolo
            no["tipo_expr"] = simbolo["tipo"] if simbolo is not None else ERRO
        elif no["tipo"] == "Binaria":
            no["tipo_expr"] = tipar_binaria(no)

        return no["tipo_expr"]

    def visitar(no):
        tipo = no["tipo"]

        if tipo == "Bloco":
            no["escopo"] = len(escopos)
            escopos.append({})
            ativos.append(no["escopo"])
            for comando in no["comandos"]:
                visitar(comando)
            ativos.pop()

        elif tipo == "Declaracao":
            declarar(no)

        elif tipo == "Atribuicao":
            token = no["identificador"]
            simbolo = resolver(token)
            no["simbolo"] = simbolo
            valor = tipar(no["expressao"])
            if simbolo is not None and valor != ERRO and valor != simbolo["tipo"]:
                diagnosticar(
                    "E_TIPO", token,
                    f'Atribuição a {token["lexeme"]!r} exige {simbolo["tipo"]}, '
                    f"recebeu {valor}.",
                )

        elif tipo == "Saida":
            # Os dois tipos válidos de expressão, int e bool, são aceitos pelo print.
            tipar(no["expressao"])

        elif tipo in ("Se", "Enquanto", "Para"):
            if tipo == "Para":
                visitar(no["inicializacao"])

            condicao = tipar(no["condicao"])
            if condicao not in ("bool", ERRO):
                token = no["token"]
                diagnosticar(
                    "E_TIPO", token,
                    f'A condição de {token["lexeme"]!r} exige bool, recebeu {condicao}.',
                )

            if tipo == "Se":
                visitar(no["entao"])
                if no["senao"] is not None:
                    visitar(no["senao"])
            else:
                if tipo == "Para":
                    visitar(no["atualizacao"])
                visitar(no["corpo"])

    for comando in arvore["comandos"]:
        visitar(comando)

    return escopos, diagnosticos
