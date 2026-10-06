import matplotlib.pyplot as plt


def gerar_grafico_categoria(tabela):
    if tabela.empty:
        print("\nNão existem dados para gerar o gráfico.")
        return

    despesas = tabela[tabela["tipo"] == "Despesa"]

    if despesas.empty:
        print("\nNão existem despesas para gerar o gráfico.")
        return

    resumo = despesas.groupby("categoria")["valor"].sum()

    resumo.plot(kind="bar")

    plt.title("Despesas por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Valor (R$)")

    plt.tight_layout()
    plt.show()