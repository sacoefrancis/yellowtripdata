#!/usr/bin/env bash
./yellowtrip.sh
./pyscripts/00_depedent_script_for_python.sh
python pyscripts/01_ps_ddl_scripst.py
python pyscripts/02_data_cleansing.py
python pyscripts/03_postgres_import_to_table.py
python pyscripts/04_posgres_export_from_table.py

