"""
Pipeline completo de ETL do projeto (Etapa 2) - ESQUELETO.

Objetivo: reexecutável do zero, com validações e log das transformações.

Uso (planejado):
  python etl/run_etl.py
"""

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIR_RAW = RAIZ / "dados" / "raw"
DIR_PROC = RAIZ / "dados" / "processed"
ARQ_DW = RAIZ / "dw" / "bi_enem.duckdb"


def main():
    # 1. Extração: PIB/IPCA (extrair_pib_municipal.py), população, ENEM e Censo 2014-2023
    # 2. Transformação: filtros, padronização da chave (município, rede, localização, ano)
    # 3. Carga: dimensões e fatos no DuckDB
    # 4. Validações e log
    # 5. Exportação das tabelas agregadas (CSV) para o Tableau Public
    raise NotImplementedError("Pipeline ainda em construção (Etapa 2).")


if __name__ == "__main__":
    main()
