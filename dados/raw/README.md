# dados/raw

Arquivos brutos, exatamente como baixados das fontes. Não são versionados (ver `.gitignore`).

Estrutura esperada:

```
dados/raw/enem/MICRODADOS_ENEM_<ano>.csv              # INEP - Microdados do ENEM
dados/raw/censo/microdados_ed_basica_<ano>.csv        # INEP - Censo Escolar
dados/raw/ibge/pib_<tabela>_<ano>.json                # gerado por etl/extrair_pib_municipal.py
dados/raw/ibge/ipca_<ano>.json                        # gerado por etl/extrair_pib_municipal.py
```
