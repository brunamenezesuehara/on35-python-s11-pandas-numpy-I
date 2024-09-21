import pandas as pd

# Dados
dados = {
    'Região': [
        'Região Metropolitana',
        'Mata Norte',
        'Mata Sul',
        'Agreste',
        'Sertão de Pernambuco',
        'Sertão de São Francisco',
        'Fernando de Noronha'
    ],
    'Temperatura mínima (°C)': [24, 20, 19, 16, 16, 20, 25],
    'Temperatura máxima (°C)': [31, 31, 31, 32, 35, 35, 31],
    'Irradiação (Wh/m²)': [41390] * 7  # Usando o mesmo valor para todas as regiões
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Salvar como Excel
df.to_excel('clima_pernambuco.xlsx', index=False)
print(df)
