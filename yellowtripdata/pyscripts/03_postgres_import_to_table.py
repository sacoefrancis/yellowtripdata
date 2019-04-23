import psycopg2
import pandas as pd
import sys
import os

def pg_load_table(file_path, table_name, dbname, host, port, user, pwd):
    '''
    This function upload csv to a target table
    '''
    try:
        conn = psycopg2.connect(dbname=dbname, host=host, port=port,\
         user=user, password=pwd)
        print("Connecting to Database")
        cur = conn.cursor()
        f = open(file_path, "r")
        # Truncate the table first
        cur.execute("Truncate {} Cascade;".format(table_name))
        print("Truncated {}".format(table_name))
        # Load table from the file with header
        cur.copy_expert("copy {} from STDIN CSV NULL '' HEADER QUOTE '\"'".format(table_name), f)
        cur.execute("commit;")
        print("Loaded data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

# Configuration
dbname = 'postgres'
host = 'localhost'
port = '5432'
user = 'postgres'
pwd = 'docker'

dirName = os.path.dirname(__file__)
 
# yellow_trip
file_path = os.path.join(dirName,'../inputs/yellow_tripdata_2018-01_cleared.csv')
table_name = 'yellow_trip'

pg_load_table(file_path, table_name, dbname, host, port, user, pwd)

# taxi_zone_looup
file_path = os.path.join(dirName,'../inputs/taxi_zone_lookup.csv')
table_name = 'taxi_zone_lookup'

pg_load_table(file_path, table_name, dbname, host, port, user, pwd)
