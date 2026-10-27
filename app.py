import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Dashboard - Atividade 06",
    layout="wide",
    initial_sidebar_state="expanded",  # sidebar começa aberto e pode ser recolhido
)

# ---------------- SIDEBAR (dados do aluno) ----------------
st.sidebar.header("Informações do Aluno")
st.sidebar.write("**Nome:** Ana Clara Matias")
st.sidebar.write("**Nº da chamada:** 03")
st.sidebar.write("**Turma:** 3E2")

st.title("Dashboard - Atividade 06")

# ================= LINHA 1 =================
col1, col2, col3 = st.columns(3)

with col1:
    tb = pd.read_csv("graficosCSV/dados_barras.csv")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        data=tb,
        x="categoria",
        y="vendas_medias",
        hue="regiao",
        palette="Set2",
        errorbar=None,
        ax=ax
    )
    ax.set_title("Média de Vendas por Categoria e Região", fontsize=14, fontweight="bold")
    ax.set_xlabel("Categoria", fontsize=11)
    ax.set_ylabel("Vendas Médias", fontsize=11)
    ax.legend(title="Região", frameon=True)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write("**Análise:** A categoria Livros tem a maior média de vendas (186,8) e a região "
             "Oeste lidera no geral (225,2), enquanto o Norte tem a menor (102,5). "
             "O melhor resultado é Livros no Oeste (284,2) e o pior é Alimentos no Norte (cerca de 54).")

with col2:
    df = pd.read_csv("graficosCSV/dados_boxplot.csv")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        data=df,
        x="departamento",
        y="salario",
        palette="Set2",
        errorbar=None,
        ax=ax
    )
    ax.set_title("Média de Salario por departamento", fontsize=14, fontweight="bold")
    ax.set_xlabel("departamento", fontsize=11)
    ax.set_ylabel("salario", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write("**Análise:** Vendas (7.575) e TI (7.352) têm os maiores salários médios, "
             "quase o dobro de Marketing (4.470) e RH (4.381).")

with col3:
    df = pd.read_csv("graficosCSV/dados_pizza.csv")
    fig, ax = plt.subplots(figsize=(8, 8))
    cores = sns.color_palette('Set2', len(df))
    ax.pie(
        df['faturamento'],
        labels=df['canal_venda'],
        autopct='%1.1f%%',
        startangle=140,
        colors=cores,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
    )
    ax.set_title("Distribuição do Faturamento por Canal de Venda", fontsize=14, fontweight="bold")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write("**Análise:** O Site responde por 37,5% do faturamento e a Loja Física por 26,7%; "
             "juntos são 64,2% do total. O canal Telefone é o menor, com 6,7%.")

# ================= LINHA 2 =================
col1, col2, col3 = st.columns(3)

with col1:
    tb = pd.read_csv("graficosCSV/dados_distribuicao.csv")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(
        data=tb,
        x="idade",
        kde=True,
        bins=15,
        color="#4c72b0",
        ax=ax,
    )
    ax.set_title("Distribuição da Idade dos Clientes", fontsize=14, fontweight="bold")
    ax.set_xlabel("Idade (anos)", fontsize=11)
    ax.set_ylabel("Frequência", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write("**Análise:** As idades vão de 18 a 69 anos, com média de 33,6 e mediana de 29. "
             "A maioria dos clientes é jovem (a idade mais comum é 24 anos) e há poucos clientes mais velhos.")

with col2:
    df = pd.read_csv("graficosCSV/dados_frequencia.csv")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(
        data=df,
        x="tipo_atendimento",
        kde=True,
        bins=15,
        color="#4c72b0",
        ax=ax
    )
    ax.set_title("Tipo de atendimento dos Clientes", fontsize=14, fontweight="bold")
    ax.set_xlabel("tipo_atendimento", fontsize=11)
    ax.set_ylabel("Frequência", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write("**Análise:** Dúvida é o atendimento mais comum (116 de 300, 38,7%), seguido de "
             "Reclamação (73, 24,3%). O menos frequente é Elogio (29, 9,7%).")

with col3:
    df = pd.read_csv("graficosCSV/dados_heatmap.csv")
    matriz = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
    dias_ordenados = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    matriz = matriz.reindex([dia for dia in dias_ordenados if dia in matriz.index])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(
        matriz,
        annot=True,
        fmt="g",
        cmap="YlGnBu",
        linewidths=0.5,
        cbar_kws={'label': 'Movimento de Clientes'},
        ax=ax
    )
    ax.set_title("Movimento de Clientes por Dia e Horário", fontsize=14, fontweight="bold")
    ax.set_xlabel("Horário", fontsize=11)
    ax.set_ylabel("Dia da Semana", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write("**Análise:** O maior movimento é no domingo às 12:00 (199 clientes) e o menor na "
             "quinta às 16:00 (22). Domingo e sábado são os dias mais movimentados; quinta é o mais fraco.")

# ================= LINHA 3 =================
col1, col2, col3 = st.columns(3)

with col1:
    tb = pd.read_csv("graficosCSV/dados_linhas.csv")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        data=tb,
        x="data",
        y="vendas",
        hue="loja",
        marker="o",
        color="#2b5c8f",
        linewidth=2,
        ax=ax,
    )
    ax.set_title("Evolução do Número de vendas", fontsize=14, fontweight="bold")
    ax.set_xlabel("Vendas", fontsize=11)
    ax.set_ylabel("Lojas", fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write("**Análise:** De janeiro a março de 2026 as vendas cresceram, passando de cerca de 122 "
             "em janeiro para cerca de 225 em março. A Loja B vendeu um pouco mais em média "
             "(179) do que a Loja A (168).")

with col2:
    df = pd.read_csv("graficosCSV/dados_dispersao.csv")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x="altura_cm",
        y="peso_kg",
        hue="sexo",
        palette="Set1",
        s=70,
        ax=ax
    )
    ax.set_title("Relação entre Altura e Peso por Sexo", fontsize=14, fontweight="bold")
    ax.set_xlabel("Altura (cm)", fontsize=11)
    ax.set_ylabel("Peso (kg)", fontsize=11)
    ax.legend(title="Sexo", frameon=True)
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write("**Análise:** Quanto maior a altura, maior o peso (correlação forte, de cerca de 0,86). "
             "Homens e mulheres seguem o mesmo padrão e têm médias parecidas.")

with col3:
    df = pd.read_csv("graficosCSV/dados_regressao.csv")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.regplot(
        data=df,
        x="renda_mensal",
        y="gasto_mensal",
        color="#2b5c8f",
        line_kws={"color": "red", "linewidth": 2},
        ax=ax
    )
    ax.set_title("Relação entre Renda Mensal e Gasto Mensal", fontsize=14, fontweight="bold")
    ax.set_xlabel("Renda Mensal", fontsize=11)
    ax.set_ylabel("Gasto Mensal", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.write("**Análise:** Quem ganha mais gasta mais, com relação muito forte (correlação de 0,99). "
             "A cada 1 real a mais de renda, o gasto sobe cerca de 0,57 real; em média, o gasto "
             "é 61% da renda.")