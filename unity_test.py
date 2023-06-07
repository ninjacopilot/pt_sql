import pandas as pd

# Ler o arquivo Excel
# df = pd.read_excel('teste.xlsx')# #skiprows=1)

# for index, row in df.iterrows():
#     coluna1 = row['Project']
#     print(coluna1)

import pandas as pd

# Ler o arquivo Excel
df_original = pd.read_excel('teste.xlsx')

# Selecionar apenas as colunas desejadas
colunas_desejadas = ['Test']
df_selecionado = df_original[colunas_desejadas]

# Salvar o DataFrame selecionado em um novo arquivo Excel
df_selecionado.to_excel('novo_arquivo.xlsx', index=False)
