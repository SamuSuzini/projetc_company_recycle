import pandas as pd
from faker import Faker

# Instanciar o gerador de nomes falsos
fake = Faker()

# Carregar o arquivo Excel
file_path = 'SEU_CAMINHO_DO_ARQUIVO.xlsx'  # Mude para o caminho do seu arquivo
df = pd.read_excel(file_path)

# Nome da coluna que contém os nomes a serem falsificados
coluna_nomes = 'xxxxxxxxxxxxxxxxxxxx'  # Mude para o nome da sua coluna

# Obter os nomes únicos na coluna especificada
unique_names = df[coluna_nomes].unique()

# Gerar um nome falso para cada nome único
name_mapping = {name: fake.name() for name in unique_names}

# Substituir os nomes na coluna com os nomes falsos
df[coluna_nomes] = df[coluna_nomes].map(name_mapping)

# Salvar o DataFrame ajustado em um novo arquivo Excel
output_path = 'SEU_CAMINHO_DE_SAIDA.xlsx'  # Mude para o caminho do seu arquivo de saída
df.to_excel(output_path, index=False)

print(f"Arquivo salvo em: {output_path}")