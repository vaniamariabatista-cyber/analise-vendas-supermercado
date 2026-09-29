import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
senha = os.getenv("DB_PASSWORD")

engine = create_engine(f"postgresql+psycopg2://postgres:{senha}@localhost/analise_vendas_supermercado")

df = pd.read_sql("SELECT * FROM raw_vendas", engine)

print("=== Dimensões ===")
print(df.shape)
print(df.head())
print("\n=== Tipos antes da conversão ===")
print(df.dtypes)

# Conversão de tipos numéricos
df["Unit price"] = df["Unit price"].astype(float)
df["Quantity"] = df["Quantity"].astype(int)
df["Tax 5%"] = df["Tax 5%"].astype(float)
df["Sales"] = df["Sales"].astype(float)
df["cogs"] = df["cogs"].astype(float)
df["gross margin percentage"] = df["gross margin percentage"].astype(float)
df["gross income"] = df["gross income"].astype(float)
df["Rating"] = df["Rating"].astype(float)

# Conversão de data e hora
df["Date"] = pd.to_datetime(df["Date"])
df["Time"] = pd.to_datetime(df["Time"], format="%I:%M:%S %p").dt.time

print("\n=== Tipos depois da conversão ===")
print(df.dtypes)

print("\n=== Valores ausentes ===")
print(df.isnull().sum())

print("\n=== Linhas duplicadas ===")
print(df.duplicated().sum())

# Remove duplicidades, se houver
df = df.drop_duplicates()

# Renomeia as colunas para o padrão da camada Tratada
df = df.rename(columns={
    "Invoice ID": "id_venda",
    "Branch": "filial",
    "City": "cidade",
    "Customer type": "tipo_cliente",
    "Gender": "genero",
    "Product line": "linha_produto",
    "Unit price": "preco_unitario",
    "Quantity": "quantidade",
    "Tax 5%": "imposto",
    "Sales": "valor_total",
    "Date": "data_venda",
    "Time": "hora_venda",
    "Payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross margin percentage": "margem_percentual",
    "gross income": "receita_bruta",
    "Rating": "avaliacao",
})

print("\n=== Colunas renomeadas ===")
print(df.columns.tolist())

# Coluna derivada: dia da semana da venda
df["dia_semana"] = df["data_venda"].dt.day_name()

print("\n=== Amostra final ===")
print(df.head())

# Salva em CSV na camada processed
df.to_csv("data/processed/vendas_tratadas.csv", index=False)
print("\nCSV salvo em data/processed/vendas_tratadas.csv")

# Salva na tabela vendas_tratadas do banco
df.to_sql("vendas_tratadas", engine, if_exists="replace", index=False)
print("Dados gravados na tabela vendas_tratadas")