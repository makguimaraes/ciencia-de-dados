#%% md
Importar as bibliotecas usadas
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(df)

#%% md
Imprimir as cinco primeiras linhas
#%%

df.head()

#%% md
O número de linhas e colunas do dataframe
#%%

df.shape

#%%
df_2022 = pd.read_csv(r'D:\My Drive\Cursos\Imersão\datasets\Enem 2022\DADOS\MICRODADOS_ENEM_2022.csv', encoding='latin1', sep = ';')

df_2023 = pd.read_csv(r'D:\My Drive\Cursos\Imersão\datasets\Enem 2023\DADOS\MICRODADOS_ENEM_2023.csv', encoding='latin1', sep = ';')
#%%
# Mapeamento das faixas etárias
mapeamento_faixas_etarias = {
    1: 'Menos de 17 anos',
    2: '17',
    3: '18',
    4: '19',
    5: '20',
    6: '21',
    7: '22',
    8: '23',
    9: '24',
    10: '25',
    11: 'Entre 26 e 30 anos',
    12: 'Entre 31 e 35 anos',
    13: 'Entre 36 e 40 anos',
    14: 'Entre 41 e 45 anos',
    15: 'Entre 46 e 50 anos',
    16: 'Entre 51 e 55 anos',
    17: 'Entre 56 e 60 anos',
    18: 'Entre 61 e 65 anos',
    19: 'Entre 66 e 70 anos',
    20: 'Maior de 70 anos'
}
#%%
# Criando uma lista ordenada das faixas etárias
faixas_etarias_ordenadas = [mapeamento_faixas_etarias[i] for i in range(1, len(mapeamento_faixas_etarias) + 1)]
#%%
# Reordenando as contagens de acordo com a lista ordenada das faixas etárias
contagem_faixas_etarias_2022 = contagem_faixas_etarias_2022.reindex(faixas_etarias_ordenadas)
contagem_faixas_etarias_2023 = contagem_faixas_etarias_2023.reindex(faixas_etarias_ordenadas)
#%%
contagem_faixas_etarias_2022 = df_2022['TP_FAIXA_ETARIA'].value_counts().sort_index()
contagem_faixas_etarias_2023 = df_2023['TP_FAIXA_ETARIA'].value_counts().sort_index()
#%%
# Calculando as contagens totais para cada conjunto de dados
total_2022 = contagem_faixas_etarias_2022.sum()
total_2023 = contagem_faixas_etarias_2023.sum()
#%%

contagem_faixas_etarias_2022 = df_2022['TP_FAIXA_ETARIA'].value_counts().sort_index()
contagem_faixas_etarias_2023 = df_2023['TP_FAIXA_ETARIA'].value_counts().sort_index()

# Calculando as contagens totais para cada conjunto de dados
total_2022 = contagem_faixas_etarias_2022.sum()
total_2023 = contagem_faixas_etarias_2023.sum()

# Calculando as porcentagens de cada faixa etária para cada ano
porcentagens_2022 = contagem_faixas_etarias_2022 / total_2022 * 100
porcentagens_2023 = contagem_faixas_etarias_2023 / total_2023 * 100

# Criando um array de índices para o eixo x
x = np.arange(len(porcentagens_2022))

# Largura das barras
largura = 0.35

# Criando o gráfico de barras agrupadas
fig, ax = plt.subplots(figsize=(15, 10))
barras_2022 = ax.bar(x - largura, porcentagens_2022, largura, label='2022')
barras_2023 = ax.bar(x, porcentagens_2023, largura, label='2023')

# Adicionando rótulos e título
ax.set_ylabel('Porcentagem')
ax.set_title('Comparação de Porcentagens por Faixa Etária entre 2022 e 2023')

# Definindo os rótulos do eixo x como as faixas etárias
ax.set_xticks(x)
ax.set_xticklabels(contagem_faixas_etarias_2022.index.map(mapeamento_faixas_etarias), rotation=90)

# Adicionando uma legenda personalizada com base no mapeamento
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, title='Ano', loc='upper right')

# Adicionando as porcentagens nas barras
for barra in barras_2022:
    altura = barra.get_height()
    ax.annotate(f'{altura:.2f}%', 
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom', rotation=90)  # Rotação vertical

for barra in barras_2023:
    altura = barra.get_height()
    ax.annotate(f'{altura:.2f}%', 
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom', rotation=90)  # Rotação vertical
#%%
