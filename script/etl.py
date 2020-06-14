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
    for i in range(len(customer_data)):
        data = customer_data.values[i]
        cur.execute(query, data)


def process_geolocation_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    geo_data = df[['geolocation_zip_code_prefix', 'geolocation_lat',
                   'geolocation_lng', 'geolocation_city', 'geolocation_state']]
    for i in range(len(geo_data)):
        data = geo_data.values[i]
        cur.execute(query, data)


def process_order_items_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    oi_data = df[['order_id', 'order_item_id', 'product_id',
                  'seller_id', 'shipping_limit_date', 'price', 'freight_value']]
    for i in range(len(oi_data)):
        data = oi_data.values[i]
        cur.execute(query, data)


def process_order_payments_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    op_data = df[['order_id', 'payment_sequential', 'payment_type',
                  'payment_installments', 'payment_value']]
    for i in range(len(op_data)):
        data = op_data.values[i]
        cur.execute(query, data)


def process_order_reviews_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    or_data = df[['review_id', 'order_id', 'review_score', 'review_comment_title',
                  'review_comment_message', 'review_creation_date', 'review_answer_timestamp']]
    for i in range(len(or_data)):
        data = or_data.values[i]
        cur.execute(query, data)


def process_orders_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    or_data = df[['order_id', 'customer_id', 'order_status',
                  'order_purchase_timestamp', 'order_approved_at',
                  'order_delivered_carrier_date', 'order_delivered_customer_date',
                  'order_estimated_delivery_date']]
    for i in range(len(or_data)):
        data = or_data.values[i]
        cur.execute(query, data)


def process_products_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    p_data = df[['product_id', 'product_category_name', 'product_name_lenght', 'product_description_lenght',
                 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']]
    for i in range(len(p_data)):
        data = p_data.values[i]
        cur.execute(query, data)


def process_sellers_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    s_data = df[['seller_id', 'seller_zip_code_prefix', 'seller_city',
                 'seller_state']]
    for i in range(len(s_data)):
        data = s_data.values[i]
        cur.execute(query, data)


def process_pcnt_file(cur, conn, filename, query):
    df = pd.read_csv(filename, index_col=None, encoding='utf-8')
    pcnt_data = df[['product_category_name', 'product_category_name_english']]
    for i in range(len(pcnt_data)):
        data = pcnt_data.values[i]
        cur.execute(query, data)


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
    process_orders_file(cur=cur, conn=conn,
                        filename=filepath+'olist_orders_dataset.csv', query=query[5])
    process_products_file(cur=cur, conn=conn,
                          filename=filepath+'olist_products_dataset.csv', query=query[6])
    process_sellers_file(cur=cur, conn=conn, filename=filepath +
                         'olist_sellers_dataset.csv', query=query[7])
    process_pcnt_file(cur=cur, conn=conn, filename=filepath +
                      'product_category_name_translation.csv', query=query[8])

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
