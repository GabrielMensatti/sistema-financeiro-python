def calcular_saldo(tabela):
    receitas = tabela[tabela["tipo"] == "Receita"]["valor"].sum()
    despesas = tabela[tabela["tipo"] == "Despesa"]["valor"].sum()

    return receitas - despesas


def listar_movimentacoes(tabela):
    if tabela.empty:
        print("\nNenhuma movimentação cadastrada.")
    else:
        print("\n===== MOVIMENTAÇÕES =====")
        print(tabela.to_string(index=False))


def resumo_por_categoria(tabela):
    if tabela.empty:
        print("\nNenhuma movimentação cadastrada.")
        return

    print("\n===== RESUMO POR CATEGORIA =====")

    resumo = tabela.groupby(
        ["tipo", "categoria"]
    )["valor"].sum()

    print(resumo)


def filtrar_por_mes(tabela):
    if tabela.empty:
        print("\nNenhuma movimentação cadastrada.")
        return

    mes = input("Digite o mês (ex: 10): ")

    resultado = tabela[
        tabela["data"].astype(str).str.split("/").str[1] == mes
    ]

    if resultado.empty:
        print("\nNenhuma movimentação encontrada nesse mês.")
    else:
        print("\n===== MOVIMENTAÇÕES DO MÊS =====")
        print(resultado.to_string(index=False))


def ordenar_por_valor(tabela):
    if tabela.empty:
        print("\nNenhuma movimentação cadastrada.")
        return

    resultado = tabela.sort_values(
        by="valor",
        ascending=False
    )

    print("\n===== MOVIMENTAÇÕES ORDENADAS POR VALOR =====")
    print(resultado.to_string(index=False))