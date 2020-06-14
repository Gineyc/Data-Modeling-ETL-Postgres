# CREATE TABLES
customers_table_create = ("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id varchar PRIMARY KEY,
    customer_unique_id varchar NOT NULL,
    customer_zip_code_prefix int NOT NULL,
    customer_city varchar,
    customer_state varchar
);
""")

geolocation_table_create = ("""
CREATE TABLE IF NOT EXISTS geolocation (
    geolocation_zip_code_prefix int,
    geolocation_lat bigint NOT NULL,
    geolocation_lng int NOT NULL,
    geolocation_city varchar,
    geolocation_state varchar
);
""")

order_item_table_create = ("""
CREATE TABLE IF NOT EXISTS order_item (
    order_id varchar PRIMARY KEY,
    order_item_id int NOT NULL,
    product_id varchar NOT NULL,
    seller_id varchar NOT NULL,
    shipping_limit_date varchar NOT NULL,
    price float NOT NULL,
    freight_value float 
);
""")


order_payments_table_create = ("""
CREATE TABLE IF NOT EXISTS order_payments (
    order_id varchar PRIMARY KEY,
    payment_sequential int NOT NULL,
    payment_type varchar NOT NULL,
    payment_installments int NOT NULL,
    payment_value float NOT NULL
);
""")

order_review_table_create = ("""
CREATE TABLE IF NOT EXISTS order_review (
    review_id varchar PRIMARY KEY,
    order_id varchar NOT NULL,
    review_score int NOT NULL,
    review_comment_title varchar,
    review_comment_message varchar,
    review_creation_date varchar NOT NULL,
    review_answer_timestamp varchar NOT NULL
);
""")

orders_table_create = ("""
CREATE TABLE IF NOT EXISTS orders (
    order_id int PRIMARY KEY,
    customer_id int NOT NULL,
    order_purchase_timestamp varchar NOT NULL,
    order_approved_at varchar NOT NULL,
    order_delivered_carrier_date varchar NOT NULL,
    order_delivered_customer_date varchar NOT NULL,
    order_estimated_delivery_date varchar NOT NULL
);
""")

products_table_create = ("""
CREATE TABLE IF NOT EXISTS products (
    product_id int PRIMARY KEY,
    product_category_name varchar,
    product_name_lenght int,
    product_description_lenght int,
    product_photos_qty int,
    product_weight_g int,
    product_length_cm int,
    product_height_cm int,
    product_width_cm int
);
""")

sellers_table_create = ("""
CREATE TABLE IF NOT EXISTS sellers (
    seller_id int PRIMARY KEY,
    seller_zip_code_prefix int NOT NULL,
    seller_city varchar,
    seller_state varchar
);
""")

product_category_name_table_create = ("""
CREATE TABLE IF NOT EXISTS product_category_name (
    product_category_name varchar,
    product_category_name_english varchar
);
""")

# DROP TABLES

customers_table_drop = "DROP TABLE IF EXISTS customers"
geolocation_table_drop = "DROP TABLE IF EXISTS geolocation"
order_item_table_drop = "DROP TABLE IF EXISTS order_item"
order_payments_table_drop = "DROP TABLE IF EXISTS order_payments"
order_review_table_drop = "DROP TABLE IF EXISTS order_review"
orders_table_drop = "DROP TABLE IF EXISTS orders"
products_table_drop = "DROP TABLE IF EXISTS products"
sellers_table_drop = "DROP TABLE IF EXISTS sellers"
product_category_name = "DROP TABLE IF EXISTS product"


# INSERT RECORDS
customers_table_insert = ("""
INSERT INTO customers (
    customer_id,
    customer_unique_id ,
    customer_zip_code_prefix ,
    customer_city ,
    customer_state ) VALUES (%s,%s,%s,%s,%s)
    ;
""")

geolocation_table_insert = ("""
INSERT INTO geolocation (
    geolocation_zip_code_prefix ,
    geolocation_lat ,
    geolocation_lng ,
    geolocation_city ,
    geolocation_state 
) VALUES (%s,%s,%s,%s,%s)
;
""")

order_item_table_insert = ("""
INSERT INTO order_item (
    order_id ,
    order_item_id ,
    product_id ,
    seller_id ,
    shipping_limit_date ,
    price ,
    freight_value  
    ) VALUES (%s,%s,%s,%s,%s,%s,%s)
    ;
""")


order_payments_table_insert = ("""
INSERT INTO order_payments (
    order_id ,
    payment_sequential ,
    payment_type ,
    payment_installments ,
    payment_value 
    ) VALUES (%s,%s,%s,%s,%s) 
;
""")

order_review_table_insert = ("""
INSERT INTO order_review (
    review_id,
    order_id ,
    review_score,
    review_comment_title ,
    review_comment_message ,
    review_creation_date ,
    review_answer_timestamp 
    ) VALUES (%s,%s,%s,%s,%s,%s,%s)
    ;
""")

orders_table_insert = ("""
INSERT INTO orders (
    order_id ,
    customer_id ,
    order_purchase_timestamp ,
    order_approved_at ,
    order_delivered_carrier_date ,
    order_delivered_customer_date ,
    order_estimated_delivery_date 
    ) VALUES (%s,%s,%s,%s,%s,%s,%s)
""")

products_table_insert = ("""
INSERT INTO products (
    product_id ,
    product_category_name ,
    product_name_lenght ,
    product_description_lenght ,
    product_photos_qty ,
    product_weight_g ,
    product_length_cm ,
    product_height_cm ,
    product_width_cm 
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ;
""")

sellers_table_insert = ("""
INSERT INTO sellers (
    seller_id int PRIMARY KEY,
    seller_zip_code_prefix int NOT NULL,
    seller_city varchar,
    seller_state varchar
    ) VALUES (%s,%s,%s,%s);
""")

product_category_name_table_insert = ("""
INSERT INTO product_category_name (
    product_category_name,
    product_category_name_english 
    ) VALUES (%s,%s)
    ;
""")

table_create_lst = [customers_table_create, geolocation_table_create, order_item_table_create, order_payments_table_create,
                    order_review_table_create, orders_table_create, products_table_create, products_table_create, sellers_table_create, product_category_name_table_create]
table_drop_lst = [customers_table_drop, geolocation_table_drop, order_item_table_drop,
                  order_payments_table_drop, order_review_table_drop, orders_table_drop, products_table_drop, sellers_table_drop, product_category_name]
table_insert_lst = [customers_table_insert, geolocation_table_insert, order_item_table_insert, order_payments_table_insert,
                    order_review_table_insert, orders_table_insert, products_table_insert, products_table_insert, sellers_table_insert, product_category_name_table_insert]
