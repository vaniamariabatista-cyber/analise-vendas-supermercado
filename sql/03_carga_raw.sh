#!/bin/bash
# Carga da camada Raw. Executar a partir da raiz do projeto.
sudo -u postgres psql -d analise_vendas_supermercado -c "TRUNCATE raw_vendas;"
sudo -u postgres psql -d analise_vendas_supermercado -c "\copy raw_vendas FROM STDIN WITH (FORMAT csv, HEADER true)" < "data/raw/SuperMarket Analysis.csv"