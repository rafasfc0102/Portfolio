import pandas as pd              
import matplotlib.pyplot as plt  

caminho = ("D:/Curso_Python/portifolho/brasileirao_serie_a_2018_2025_unica_aba.xlsx")

df = pd.read_excel(caminho)

print(df.head())

print("\nColunas disponíveis:")
print(df.columns)

print("\nInformações gerais:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())




# GRÁFICO DE BARRAS - BRASILEIRÃO 2025 

df_2025 = df[df['Ano'] == 2025]

df_2025 = df_2025.sort_values(by='Points', ascending=False)

cores = ['royalblue', 'orange', 'green', 'red', 'purple', 'gold', 
          'cyan', 'magenta', 'lime', 'pink', 'brown', 
         'gray', 'teal', 'navy', 'salmon', 'olive', 'plum', 'darkred', 'deepskyblue', 'black']

fig, ax = plt.subplots()

barras = ax.bar(df_2025['Team'], df_2025['Points'], color=cores[:len(df_2025)])

ax.bar_label(barras, labels=[f'{p}' for p in df_2025['Points']], 
              padding=3, fontsize=9, color='black', weight='bold')

plt.title('Pontos por Time - Brasileirão 2025')
plt.xlabel('Time')
plt.ylabel('Pontos')
plt.xticks(rotation=90)
plt.show()




# GRÁFICO DE LINHA - EVOLUÇÃO DOS PONTOS

time = 'Santos'

df_time = df[df['Team'] == time]

plt.plot(df_time['Ano'], df_time['Points'], marker='o')
plt.title(f'Evolução dos Pontos - {time}')
plt.xlabel('Ano')
plt.ylabel('Pontos')
plt.show()




# GRÁFICO DE DISPERSÃO - GOLS FEITOS x SOFRIDOS

plt.scatter(df['GoalsFor'], df['GoalsAgainst'])
plt.title('Gols Feitos x Gols Sofridos')
plt.xlabel('Gols Feitos')
plt.ylabel('Gols Sofridos')
plt.show()




# GRÁFICO DE LINHAS - PONTOS 2025

df_2025 = df[df['Ano'] == 2025]

df_2025 = df_2025.sort_values(by='Points', ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(df_2025['Team'], df_2025['Points'], color='royalblue', marker='o', linewidth=2)

for i, p in enumerate(df_2025['Points']):
    ax.text(i, p + 0.5, str(p), ha='center', fontsize=9, color='black', weight='bold')

plt.title('Pontos por Time - Brasileirão 2025', fontsize=14, weight='bold')
plt.xlabel('Time')
plt.ylabel('Pontos')
plt.xticks(rotation=90)

plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
