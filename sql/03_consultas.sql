-- Total de vendas por linha de produto
SELECT "Product line",
       COUNT(*) AS qtd_vendas,
       SUM("Sales"::NUMERIC) AS total_vendas
FROM raw_vendas
GROUP BY "Product line"
ORDER BY total_vendas DESC;

-- Avaliações acima de 8
SELECT "Invoice ID", "Branch", "Rating"::NUMERIC AS avaliacao
FROM raw_vendas
WHERE "Rating"::NUMERIC > 8
ORDER BY avaliacao DESC;

-- Avaliação média por filial
SELECT "Branch",
        AVG("Rating"::NUMERIC) AS avaliacao_media
FROM raw_vendas
GROUP BY "Branch"
ORDER BY avaliacao_media DESC;

\copy (SELECT "Product line", COUNT(*) AS qtd_vendas, SUM("Sales"::NUMERIC) AS total_vendas FROM raw_vendas GROUP BY "Product line" ORDER BY total_vendas DESC) TO 'data/raw/vendas_por_categoria.csv' WITH (FORMAT csv, HEADER true);