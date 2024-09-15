import pandas as pd
from prefect import task

@task
def carregar_dados(caminho: str):
    return pd.read_csv(caminho)

@task
def preprocessar_dados(df: pd.DataFrame):
    # Simplificado para o exemplo
    df['atraso'] = (df['atraso_chegada'] > 15).astype(int)
    features = ['dia_semana', 'mes', 'distancia']
    X = df[features]
    y = df['atraso']
    return X, y