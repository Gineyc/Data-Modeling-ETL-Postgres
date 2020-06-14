import os
import numpy as np
import psycopg2
import pandas as pd
from queries import *
from queries import table_insert_lst


def process_customer_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    customer_data = df[['customer_id', 'customer_unique_id',
                        'customer_zip_code_prefix', 'customer_city', 'customer_state']]
    for i in range(10):
        data = customer_data.values[i]
        cur.execute(query, data)


def process_geolocation_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    geo_data = df[['geolocation_zip_code_prefix', 'geolocation_lat',
                   'geolocation_lng', 'geolocation_city', 'geolocation_state']]
    for i in range(10):
        data = geo_data.values[i]
        cur.execute(query, data)


def process_order_items_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    oi_data = df[['order_id', 'order_item_id', 'product_id',
                  'seller_id', 'shipping_limit_date', 'price', 'freight_value']]
    for i in range(10):
        data = oi_data.values[i]
        cur.execute(query, data)


def process_order_payments_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    oi_data = df[['order_id', 'payment_sequential', 'payment_type',
                  'payment_installments', 'payment_value']]
    for i in range(10):
        data = oi_data.values[i]
        cur.execute(query, data)


def process_order_reviews_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    or_data = df[['review_id', 'order_id', 'review_score', 'review_comment_title',
                  'review_comment_message', 'review_creation_date', 'review_answer_timestamp']]
    for i in range(10):
        data = or_data.values[i]
        cur.execute(query, data)


def process_data(cur, conn, filepath):
    filePath = filepath
    filename = [filePath + '\\'+i for i in os.listdir(filePath)]
    for i in list(zip(table_insert_lst, filename)):
        query, filename = i
        process_file(cur, filename=filename, query=query)


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=ecommerce user=postgres password=password")

    cur = conn.cursor()
    filepath = "data\e-commerce"+"\\"
    query = table_insert_lst
    process_customer_file(cur=cur, conn=conn,
                          filename=filepath+'olist_customers_dataset.csv', query=query[0])
    process_geolocation_file(cur=cur, conn=conn,
                             filename=filepath+'olist_geolocation_dataset.csv', query=query[1])
    process_order_items_file(cur=cur, conn=conn,
                             filename=filepath+'olist_order_items_dataset.csv', query=query[2])
    process_order_payments_file(cur=cur, conn=conn,
                                filename=filepath+'olist_order_payments_dataset.csv', query=query[3])
    process_order_reviews_file(cur=cur, conn=conn,
                               filename=filepath+'olist_order_reviews_dataset.csv', query=query[4])

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
