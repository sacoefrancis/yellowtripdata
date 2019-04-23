import psycopg2
import pandas as pd
import sys


def pg_create_table(dbname, host, port, user, pwd):
    '''
    This function upload csv to a target table
    '''


    try:
        conn = psycopg2.connect(dbname=dbname, host=host, port=port, user=user, password=pwd)
        print("Connecting to Database")
        cur = conn.cursor()
        commands = ("""create table if not exists yellow_trip
                 (
                    VendorID numeric,
                    tpep_pickup_datetime timestamp,
                    tpep_dropoff_datetime timestamp,
                    passenger_count numeric,
                    trip_distance numeric,
                    RatecodeID numeric,
                    store_and_fwd_flag varchar, 
                    PULocationID numeric,
                    DOLocationID numeric,
                    payment_type numeric,
                    fare_amount numeric,
                    extra numeric,
                    mta_tax numeric,
                    tip_amount numeric,
                    tolls_amount numeric,
                    improvement_surcharge numeric,
                    total_amount numeric
                 )""",
                """create index if not exists idx_yellotrip_doloc on yellow_trip(DOLocationID)""",
                """create index if not exists idx_yelltri_cmp_trpdis on yellow_trip(trip_distance,tpep_dropoff_datetime)""",
                """create table  if not exists  taxi_zone_lookup
                (
                LocationID numeric,
                Borough varchar,
                Zone varchar,
                service_zone varchar
                )""",
                "commit;")
        for command in commands:
            cur.execute(command)

        conn.close()
        print("DB connection closed.")

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)


dbname = 'postgres'
host = 'localhost'
port = '5432'
user = 'postgres'
pwd = 'docker'

pg_create_table(dbname, host, port, user, pwd)
