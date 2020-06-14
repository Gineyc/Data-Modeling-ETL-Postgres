import os
import numpy as np
import psycopg2
import pandas as pd
from queries import *
from queries import table_insert_lst
filepath = ["data\e-commerce"+"\\" +
            i for i in os.listdir("data\e-commerce")]

print(filepath[2])
df = pd.read_csv(filepath[2], index_col=None)
print(df.columns)
"""
conn = psycopg2.connect(
    "host=127.0.0.1 dbname=ecommerce user=postgres password=password")
conn.autocommit = True
cur = conn.cursor()

filename = 'D:\\Master\\REPO\\Data Modeling\\data\\e-commerce\\olist_geolocation_dataset.csv'
query = table_insert_lst[1]

df = pd.read_csv(filename, index_col=None, encoding='utf-8')
geo_data = df[['geolocation_zip_code_prefix', 'geolocation_lat',
               'geolocation_lng', 'geolocation_city', 'geolocation_state']]
for i in range(10):
    data = geo_data.values[i]
    print(data)
    cur.execute(query, data)


conn.close()
"""
