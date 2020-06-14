from queries import *
from queries import table_create_lst, table_drop_lst
import psycopg2


def create_database():
    # connect to default database "postgre"
    conn = psycopg2.connect(
        ("host=127.0.0.1 dbname=postgres user=postgres password=password"))
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    print(cur)
    # create ecommerce database, encoding = utf-8
    cur.execute("DROP DATABASE IF EXISTS ecommerce")
    cur.execute(
        "CREATE DATABASE ecommerce WITH ENCODING 'utf8' TEMPLATE template0")
    conn.close()
    # connect to ecommerce database and return cur and conn
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=ecommerce user=postgres password=password")
    cur = conn.cursor()

    return cur, conn


def create_tables(cur, conn):

    for query in table_create_lst:
        cur.execute(query)
        conn.commit()


def drop_tables(cur, conn):

    for query in table_drop_lst:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.close()


if __name__ == "__main__":
    main()
