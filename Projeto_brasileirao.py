import pandas as pd              
import matplotlib.pyplot as plt  
import seaborn as sns


caminho = ("D:/Curso_Python/portifolho/brasileirao_serie_a_2018_2025_unica_aba.xlsx")
df = pd.read_excel(caminho)

print(df.head())
print(df.info())
print(df.isna().sum())
print(df.describe())

######################

df.columns = df.columns.str.strip()

df["Aproveitamento %"] = (df["Points"] / (df["Played"] * 3)) * 100

df["Aproveitamento %"] = df["Aproveitamento %"].round(2)

print(df.head())

######################

# time com mais vitoria
vitoria = df.groupby("Team")["Wins"].sum().reset_index()

vitoria = vitoria.sort_values(by="Wins", ascending=False).reset_index(drop=True)
print(vitoria)

# media de pontos por temporada
media_pontos = df.groupby(["Ano", "Team"])["Points"].mean()
print(media_pontos)

#Encontrar o time mais constante
menor_variacao = df.groupby('Team')['Ano'].std().reset_index()

menor_variacao = menor_variacao.sort_values(by="Ano", ascending=False).reset_index(drop=True)
print(menor_variacao)

# Analisar correlação entre gols feitos, gols sofridos e pontos
colunas = ["GoalsFor", "GoalsAgainst", "Points"]
dados_gols=df[colunas]

correlacao = dados_gols.corr().reset_index()
print(correlacao)

# Ranking geral somando pontuação de todos os anos
pontuacao_geral = df.groupby("Ano")["Points"].sum().reset_index()

pontuacao_geral = pontuacao_geral.sort_values(by="Points", ascending=False).reset_index(drop=True)
print(pontuacao_geral)

# Grafico de barras com os top 10 times com mais vitórias em um ano específico
ano_escolhido = 2022
dados_ano = df[df["Ano"] == ano_escolhido ]

top10_vitorias = dados_ano.sort_values(by="Wins", ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(top10_vitorias["Team"], top10_vitorias["Wins"], color = "royalblue")
for i, v in enumerate(top10_vitorias["Wins"]):
    plt.text(i, v + 0.3, str(v), ha="center", fontweight="bold")
plt.xlabel("Time")
plt.ylabel("Vitórias")
plt.xticks(rotation =45)
plt.tight_layout()
plt.show()

# # Gráfico de linhas mostrando a evolução dos pontos de um time ao longo dos anos.

def plot_team_points(df, team_name):
    df_team = df[df["Team"].str.lower() == team_name.lower()].copy()
    df_team = df_team.sort_values("Ano")

    plt.figure(figsize=(10,5))
    plt.plot(df_team["Ano"], df_team["Points"], marker='o', color='royalblue', linewidth=2)

    # Adicionar rótulos de pontos
    for x, y in zip(df_team["Ano"], df_team["Points"]):
        plt.text(x, y + 0.5, str(y), ha='center', va='bottom', fontweight='bold')

    plt.title(f"Evolução dos Pontos — {team_name}", fontsize=14, fontweight='bold')
    plt.xlabel("Ano", fontsize=12)
    plt.ylabel("Pontos", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(df_team["Ano"])
    plt.tight_layout()
    plt.show()

# Gerar gráfico para o Santos
plot_team_points(df, "Santos")
    
