import pandas as pd

ARQUIVO = "movimentacoes.csv"


def salvar_dados(tabela):
    tabela.to_csv(ARQUIVO, index=False)


def carregar_dados():
    try:
        return pd.read_csv(ARQUIVO)
    except FileNotFoundError:
        return pd.DataFrame({
            "data": [],
            "tipo": [],
            "descricao": [],
            "categoria": [],
            "valor": []
        })