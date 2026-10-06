#  Sistema Financeiro

Sistema de controle financeiro desenvolvido em **Python** como projeto acadêmico da disciplina de programação.

O sistema permite cadastrar receitas e despesas, consultar movimentações, calcular o saldo, analisar os dados por categoria e mês, ordenar valores e visualizar um gráfico das despesas.

---

##  Objetivo

O objetivo do projeto é desenvolver um sistema simples de controle financeiro utilizando conceitos de programação em Python e bibliotecas para manipulação e análise de dados.

O projeto também busca aplicar na prática conceitos como:

- Estruturas condicionais;
- Estruturas de repetição;
- Funções;
- Manipulação de dados;
- DataFrames;
- Leitura e gravação de arquivos;
- Agrupamento e filtragem de dados;
- Visualização de informações através de gráficos.

---

##  Funcionalidades

O sistema possui as seguintes funcionalidades:

### 1. Cadastrar receita
Permite registrar uma entrada financeira informando:

- Data;
- Descrição;
- Categoria;
- Valor.

### 2. Cadastrar despesa
Permite registrar uma saída financeira informando:

- Data;
- Descrição;
- Categoria;
- Valor.

### 3. Listar movimentações
Exibe todas as receitas e despesas cadastradas no sistema.

### 4. Consultar saldo
Calcula automaticamente o saldo atual com base nas receitas e despesas cadastradas.

**Fórmula:**

`Saldo = Receitas - Despesas`

### 5. Resumo por categoria
Utiliza o Pandas para agrupar e apresentar os valores de acordo com o tipo e a categoria da movimentação.

### 6. Gráfico de despesas
Gera um gráfico de barras mostrando o total das despesas agrupadas por categoria.

### 7. Filtrar por mês
Permite consultar as movimentações cadastradas em determinado mês.

### 8. Ordenar por valor
Organiza as movimentações em ordem decrescente de valor.

### 9. Armazenamento dos dados
Os dados são salvos em um arquivo `.csv`, permitindo que as movimentações continuem disponíveis mesmo após fechar o programa.

---

##  Tecnologias utilizadas

- **Python**
- **Pandas**
- **Matplotlib**
- **Git**
- **GitHub**

---

##  Bibliotecas utilizadas

### Pandas

Utilizado para:

- Criar e manipular DataFrames;
- Armazenar as movimentações;
- Calcular receitas e despesas;
- Agrupar dados por categoria;
- Filtrar movimentações;
- Ordenar valores;
- Ler e salvar os dados em CSV.

### Matplotlib

Utilizado para gerar os gráficos de despesas por categoria.

---

## Estrutura do projeto

```text
sistema-financeiro-python/
│
├── main.py
├── dados.py
├── financeiro.py
├── graficos.py
├── exportacao.py
├── README.md
└── .gitignore
