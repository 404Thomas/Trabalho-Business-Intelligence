# Business Intelligence: ENEM × Infraestrutura Escolar × PIB Municipal (2014–2023)

Trabalho da disciplina COM11075 – Tópicos Especiais em Banco de Dados II (UFES).

**Pergunta de negócio:** em que medida a infraestrutura das escolas e o contexto econômico do município explicam o desempenho no ENEM (2014–2023)?

## Fontes de dados

| Fonte | Origem | Formato |
|---|---|---|
| Microdados do ENEM | INEP | CSV |
| Censo Escolar (Educação Básica) | INEP | CSV |
| PIB dos Municípios (tabela 5938) | IBGE / SIDRA | API JSON |
| IPCA (tabela 1737), para deflacionar o PIB | IBGE / SIDRA | API JSON |

## Arquitetura

```
Fontes (INEP, IBGE) → Python (etl/) → dados/raw → dados/processed → DW em DuckDB (dw/) → CSVs agregados → Tableau Public
```

## Estrutura do repositório

| Pasta | Conteúdo |
|---|---|
| `dados/` | Dados brutos (`raw/`) e tratados (`processed/`); não versionados |
| `docs/` | Documentação e perfilamento das bases |
| `etl/` | Scripts Python de extração, transformação e carga |
| `dw/` | Scripts SQL do Data Warehouse (DuckDB) |
| `dashboards/` | Dashboards (Tableau Public) |
| `apresentacoes/` | Slides de cada etapa |
| `referencias/` | Dicionários de dados e referências |

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install pandas requests duckdb

python etl/extrair_pib_municipal.py   # PIB municipal deflacionado
python etl/run_etl.py                 # pipeline completo (em construção)
```

## Etapas

- [x] Etapa 1: bases, KPIs e modelo dimensional (`apresentacoes/ApresentacaoEtapa1.pdf`)
- [ ] Etapa 2: Data Warehouse e ETL
- [ ] Etapa 3: dashboards e documentação final
