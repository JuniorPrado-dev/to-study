import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import os

# Configuração do Banco
db_engine = create_engine('sqlite:///warehouse_clean.db')

def gerar_csv_sujo(filename, num_rows):
    print(f"Gerando {num_rows} linhas de dados SUJOS...")
    
    # 1. Dados Base
    ids = np.arange(1, num_rows + 1)
    # Categorias com sujeira: espaços extras e casing misturado
    cats_sujas = ['Eletrônicos', 'eletrônicos', '  ELETRÔNICOS  ', 'Roupas', 'roupas', 'CASA', '  Casa ']
    categorias = np.random.choice(cats_sujas, num_rows)
    
    # Valores (com alguns NaNs - Not a Number)
    valores = np.random.uniform(10.0, 1000.0, num_rows)
    # Introduzindo 10% de valores nulos (erros de sistema)
    indices_nulos = np.random.choice(np.arange(num_rows), size=int(num_rows * 0.10), replace=False)
    valores[indices_nulos] = np.nan 
    
    dates = pd.date_range(start='2023-01-01', periods=num_rows, freq='min')
    
    df = pd.DataFrame({
        'id_venda': ids,
        'data': dates,
        'categoria': categorias,
        'valor': valores
    })
    
    # 2. Introduzindo Duplicatas
    # Pegamos 5% das linhas e duplicamos no final
    duplicatas = df.sample(frac=0.05)
    df = pd.concat([df, duplicatas])
    
    # Misturar tudo para não ficar óbvio
    df = df.sample(frac=1).reset_index(drop=True)
    
    # Salvando
    df.to_csv(filename, index=False)
    print(f"Arquivo '{filename}' criado com {len(df)} linhas (incluindo sujeira).")

csv_file = 'vendas_sujas.csv'
gerar_csv_sujo(csv_file, 1000000)