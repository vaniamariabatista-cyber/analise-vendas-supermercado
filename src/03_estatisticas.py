import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/vendas_tratadas.csv")

print("=== ESTATÍSTICA DESCRITIVA GERAL ===")
print(df.describe())

respostas = {}

# 1. Qual filial apresentou o maior faturamento?
faturamento_filial = df.groupby("filial")["valor_total"].sum().sort_values(ascending=False)
print("\n=== Faturamento por filial ===")
print(faturamento_filial)
respostas["filial_maior_faturamento"] = faturamento_filial.idxmax()

# 2. Qual filial realizou a maior quantidade de vendas?
vendas_filial = df.groupby("filial")["id_venda"].count().sort_values(ascending=False)
print("\n=== Quantidade de vendas por filial ===")
print(vendas_filial)
respostas["filial_maior_qtd_vendas"] = vendas_filial.idxmax()

# 3. Qual linha de produto apresentou o maior faturamento?
faturamento_produto = df.groupby("linha_produto")["valor_total"].sum().sort_values(ascending=False)
print("\n=== Faturamento por linha de produto ===")
print(faturamento_produto)
respostas["produto_maior_faturamento"] = faturamento_produto.idxmax()

# 4. Qual linha de produto recebeu a melhor avaliação média?
avaliacao_produto = df.groupby("linha_produto")["avaliacao"].mean().sort_values(ascending=False)
print("\n=== Avaliação média por linha de produto ===")
print(avaliacao_produto)
respostas["produto_melhor_avaliacao"] = avaliacao_produto.idxmax()

# 5. Qual foi a forma de pagamento mais utilizada?
forma_pagamento = df["forma_pagamento"].value_counts()
print("\n=== Forma de pagamento mais utilizada ===")
print(forma_pagamento)
respostas["forma_pagamento_mais_usada"] = forma_pagamento.idxmax()

# 6. Qual foi o valor médio das vendas?
valor_medio = df["valor_total"].mean()
print(f"\n=== Valor médio das vendas: {valor_medio:.2f} ===")
respostas["valor_medio_vendas"] = round(valor_medio, 2)

# 7. Qual foi a maior venda registrada?
maior_venda = df.loc[df["valor_total"].idxmax()]
print("\n=== Maior venda registrada ===")
print(maior_venda)
respostas["maior_venda_valor"] = round(maior_venda["valor_total"], 2)
respostas["maior_venda_id"] = maior_venda["id_venda"]

# 8. Em qual dia da semana ocorreu a maior quantidade de vendas?
vendas_dia_semana = df["dia_semana"].value_counts()
print("\n=== Quantidade de vendas por dia da semana ===")
print(vendas_dia_semana)
respostas["dia_semana_mais_vendas"] = vendas_dia_semana.idxmax()

# Salva as respostas em CSV
respostas_df = pd.DataFrame(list(respostas.items()), columns=["metrica", "valor"])
respostas_df.to_csv("resultados/estatisticas/metricas.csv", index=False)
print("\n=== Métricas salvas em resultados/estatisticas/metricas.csv ===")
print(respostas_df)

# Gráfico 1: Faturamento por filial
plt.figure(figsize=(8, 5))
faturamento_filial.plot(kind="bar", color="steelblue")
plt.title("Faturamento por Filial")
plt.xlabel("Filial")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("resultados/graficos/faturamento_filiais.png")
plt.close()

# Gráfico 2: Avaliação média por produto
plt.figure(figsize=(8, 5))
avaliacao_produto.sort_values().plot(kind="barh", color="seagreen")
plt.title("Avaliação Média por Linha de Produto")
plt.xlabel("Avaliação média")
plt.ylabel("Linha de produto")
plt.tight_layout()
plt.savefig("resultados/graficos/avaliacao_produtos.png")
plt.close()

print("\n=== Gráficos salvos em resultados/graficos/ ===")