

Loading Data from https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page 2018/January data
Below activities done in this project

    Data ingestion
    Data cleanising
    Data Tranformation and Analysis

System Requirements

OS: Ubuntu
python version: 3
platform: Docker
CSV file download : need to place CSV file in inputs folder from https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page 2018/January data
The project is in yellowtripdata folder it will have below folder

1.inputs (required input files should be loaded from above link)
2.outputs (generated output will be placed in this folder)
3.pyscripts (will have below files will be executed automatically by ‘runnable.sh’)

Pyscripts folder files:

    00_depedent_script_for_python.sh - will install python and all dependent python objects

    01_ps_ddl_scripst.py - will create DDLs needs to created in postgres(postgres and its dependencies will be installed by (yellowtrip.sh)

    02_data_cleansing.py - input file csv will be cleanised by this file and new clean csv will be generated

    03_postgres_import_to_table.py - will load the data into postgress for processing

    04_posgres_export_from_table.py - will analyze the data and export the result to outputs folder in csv.

[Important note:]

runnable.sh is the only file which needs to be executed (it will invoke all the scripts mentioned above)

yellowtripdata folder should have read and write access to all files inside

