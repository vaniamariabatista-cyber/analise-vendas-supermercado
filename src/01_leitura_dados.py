import pandas as pd

import pandas as pd

arquivo = "data/raw/SuperMarket Analysis.csv"
df = pd.read_csv(arquivo)

print("=== DIMENSÕES DO DATASET ===")
print(df.shape)

print("\n=== COLUNAS ===")
print(df.columns)

print("\n=== TIPOS DE DADOS ===")
print(df.dtypes)

print("\n=== VALORES AUSENTES ===")
print(df.isnull().sum())

print("\n=== ESTATÍSTICAS DESCRITIVAS ===")
print(df.describe())

print("\n=== CATEGORIAS ===")

print("\n=== Cidade: ===")
print(df['City'].unique())

print("\n=== Tipo de Cliente: ===")
print(df['Customer type'].unique())

print("\n=== Categorias de Produto: ===")
print(df['Product line'].unique())

print("\n=== Formas de Pagamento: ===")
print(df['Payment'].unique())

print("\n=== QUANTIDADE DE VENDAS POR CATEGORIA DE PRODUTO ===")
print(df["Product line"].value_counts())


vendas_categoria = pd.read_csv("data/raw/vendas_por_categoria.csv")

print("=== Vendas por categoria (exportado do PostgreSQL) ===")
print(vendas_categoria.head())
print(vendas_categoria.info())
print(vendas_categoria.describe())