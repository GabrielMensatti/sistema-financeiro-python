import pandas as pd


def criar_tabela():
    dados = {
        "data": [],
        "tipo": [],
        "descricao": [],
        "categoria": [],
        "valor": []
    }

    return pd.DataFrame(dados)


def adicionar_movimentacao(tabela, data, tipo, descricao, categoria, valor):
    nova_movimentacao = {
        "data": data,
        "tipo": tipo,
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor
    }

    tabela.loc[len(tabela)] = nova_movimentacao

    return tabela