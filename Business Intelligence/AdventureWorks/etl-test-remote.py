# import libraries
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os

# get id and password from environment variables
pwd = os.environ['pgpass']
uid = os.environ['pguid']

# sql db details
driver = '{SQL Server Native Client 11.0}'
server = 'DESKTOP-VG2LHTB'
database = 'AdventureWorksDW2019;'

# extract data from sql server
def extract():
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+uid+';PWD='+pwd)
        cursor = conn.cursor()
        # execute query
        cursor.execute("""

            select t.name as table_name
            from sys.tables t where t.name in ('DimProduct','DimProductSubcategory','DimProductCategory','DimSalesTerritory','DimSalesReason','FactInternetSales','FactInternetSalesReason')

        """)
        tables = cursor.fetchall()
        for t in tables:
            # query and load save data to dataframe
            df = pd.read_sql_query(f'select * FROM {t[0]}', conn)
            load(df, t[0])
    except Exception as e:
        print('Extract error: '+str(e))
    finally:
        print('Closing Connection')
        conn.close()

# load data to postgres
def load(df, t):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql+pg8000://{uid}:{pwd}@34.128.70.188/AdventureWorks')
        print(f'importing rows {rows_imported} to {rows_imported+len(df)}... for table {t}')
        # save df to postgres (truncate and load)
        df.to_sql(f'stg_{t}', engine, if_exists='replace', index=False)
        rows_imported += len(df)
        # add elapsed time to final print out
        print('Data imported successful')
    except Exception as e:
        print('Load error: '+str(e))
        
try:
    # call extract function
    extract()
except Exception as e:
    print('Error while extracting: '+str(e))