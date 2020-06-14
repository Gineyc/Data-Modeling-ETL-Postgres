import os
import numpy as np
import psycopg2
import pandas as pd
from queries import *
from queries import table_insert_lst
conn = psycopg2.connect(
    "host=127.0.0.1 dbname=ecommerce user=postgres password=password")
cur = conn.cursor()


def process_geolocation_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    geo_data = df[['geolocation_zip_code_prefix', 'geolocation_lat',
                   'geolocation_lng', 'geolocation_city', 'geolocation_state']]
    for i in range(len(geo_data)):
        data = geo_data.values[i]
        cur.execute(query, data)


process_geolocation_file(
    cur, conn, filename='D:\\Master\\REPO\\Data Modeling\\data\\e-commerce\\olist_geolocation_dataset.csv', query=table_insert_lst[1])


conn.close()
