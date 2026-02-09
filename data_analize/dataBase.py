import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuração: Quantas linhas você quer?
NUM_LINHAS = 10000 

print(f"Gerando {NUM_LINHAS} registros... Aguarde.")

# Listas para gerar aleatoriedade
estados_base = ['SP', 'RJ', 'MG', 'SC', 'RS', 'PR', 'BA', 'AM']
formatos_data = ['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']

dados = {
    'id_venda': [],
    'data': [],
    'valor_venda': [],
    'estado_cliente': []
}

# Loop para gerar os dados
for i in range(1, NUM_LINHAS + 1):
    # 1. ID Sequencial
    dados['id_venda'].append(1000 + i)
    
    # 2. Datas com formatos misturados (O pesadelo do Analista de Dados)
    data_base = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
    formato_escolhido = random.choice(formatos_data)
    dados['data'].append(data_base.strftime(formato_escolhido))
    
    # 3. Valor da Venda (Com 5% de chance de vir Vazio/NaN)
    if random.random() < 0.05: # 5% de erro
        dados['valor_venda'].append(np.nan)
    else:
        valor = round(random.uniform(50.0, 5000.0), 2)
        dados['valor_venda'].append(valor)
    
    # 4. Estados (Misturando maiúsculas e minúsculas)
    estado = random.choice(estados_base)
    if random.random() < 0.3: # 30% de chance de vir minúsculo (ex: 'sp')
        dados['estado_cliente'].append(estado.lower())
    else:
        dados['estado_cliente'].append(estado)

# Criar DataFrame e Salvar
df = pd.DataFrame(dados)
nome_arquivo = 'vendas_bigdata.csv'
df.to_csv(nome_arquivo, index=False)

print(f"Sucesso! Arquivo '{nome_arquivo}' criado com {NUM_LINHAS} linhas.")
print(df.head(10)) # Mostra as primeiras 10 para conferência