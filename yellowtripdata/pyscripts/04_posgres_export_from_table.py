import psycopg2
import pandas as pd
import sys
import os

def table_to_csv(sql, file_path, dbname, host, port, user, pwd):
    '''
    This function creates a csv file from PostgreSQL with query
    '''
    try:
        conn = psycopg2.connect(dbname=dbname, host=host, port=port,\
         user=user, password=pwd)
        print("Connecting to Database")
        # Get data into pandas dataframe
        df = pd.read_sql(sql, conn)
        # Write to csv file
        df.to_csv(file_path, encoding='utf-8', header = True,\
         doublequote = True, sep=',', index=False)
        print("CSV File has been created")
        conn.close()

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

# Execution Example with transaction table
dbname = 'postgres'
host = 'localhost'
port = '5432'
user = 'postgres'
pwd = 'docker'

dirName = os.path.dirname(__file__)
 


#Query:1
sql_high_tips = ''' 
        select b.Borough, b.Zone, total_tip from 
        (select DOLocationID, round(sum(tip_amount),8) total_tip from yellow_trip 
            group by DOLocationID order by sum(tip_amount) desc limit 5) a,  
        taxi_zone_lookup b 
        where a.DOLocationID = b.LocationID
        order by  total_tip desc
        '''
file_path = os.path.join(dirName,'../outputs/top_tipping_zones.csv')   
table_to_csv(sql_high_tips, file_path, dbname, host, port, user, pwd)


#Query:2
sql_long_distance = '''
    select a.dt,a.tpep_dropoff_datetime, b.Borough, b.Zone ,a.trip_distance   from 
        (select DOLocationID, date(tpep_dropoff_datetime) dt , tpep_dropoff_datetime ,trip_distance, row_number() over (partition by date(tpep_dropoff_datetime) order by trip_distance desc) rnum from yellow_trip 
        where tpep_dropoff_datetime >= to_date('2018-01-01','yyyy-mm-dd') and tpep_dropoff_datetime < to_date('2018-01-08','yyyy-mm-dd') and  DOLocationID not in (264,265) ) a, taxi_zone_lookup b 
    where a.rnum <=5 and a.DOLocationID = b.LocationID
    '''
file_path = os.path.join(dirName,'../outputs/longest_trips_per_day.csv') 
table_to_csv(sql_long_distance, file_path, dbname, host, port, user, pwd)
