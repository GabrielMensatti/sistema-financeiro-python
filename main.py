from dados import criar_tabela, adicionar_movimentacao
from financeiro import (
    calcular_saldo,
    listar_movimentacoes,
    resumo_por_categoria,
    filtrar_por_mes,
    ordenar_por_valor
)
from exportacao import salvar_dados, carregar_dados
from graficos import gerar_grafico_categoria


tabela = carregar_dados()

if tabela.empty:
    tabela = criar_tabela()


while True:

    print("\n===== MEU CONTROLE FINANCEIRO =====")
    print("1 - Cadastrar receita")
    print("2 - Cadastrar despesa")
    print("3 - Listar movimentações")
    print("4 - Ver saldo")
    print("5 - Resumo por categoria")
    print("6 - Gráfico de despesas")
    print("7 - Filtrar por mês")
    print("8 - Ordenar por valor")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        data = input("Data: ")
        descricao = input("Descrição: ")
        categoria = input("Categoria: ")
        valor = float(input("Valor R$: "))

        tabela = adicionar_movimentacao(
            tabela,
            data,
            "Receita",
            descricao,
            categoria,
            valor
        )

        salvar_dados(tabela)

        print("\nReceita cadastrada com sucesso!")


    elif opcao == "2":

        data = input("Data: ")
        descricao = input("Descrição: ")
        categoria = input("Categoria: ")
        valor = float(input("Valor R$: "))

        tabela = adicionar_movimentacao(
            tabela,
            data,
            "Despesa",
            descricao,
            categoria,
            valor
        )

        salvar_dados(tabela)

        print("\nDespesa cadastrada com sucesso!")


    elif opcao == "3":

        listar_movimentacoes(tabela)


    elif opcao == "4":

        saldo = calcular_saldo(tabela)

        print(f"\nSaldo atual: R$ {saldo:.2f}")


    elif opcao == "5":

        resumo_por_categoria(tabela)


    elif opcao == "6":

        gerar_grafico_categoria(tabela)


    elif opcao == "7":

        filtrar_por_mes(tabela)


    elif opcao == "8":

        ordenar_por_valor(tabela)


    elif opcao == "9":

        print("\nSistema encerrado.")
        break


    else:

        print("\nOpção inválida. Tente novamente.")