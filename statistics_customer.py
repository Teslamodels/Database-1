import psycopg2
from psycopg2 import Error


def create_table_statistics_customer():
    try:
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'Greate_company')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE statistics_customer(
                        ID SERIAL PRIMARY KEY,
                        full_name VARCHAR(1000) NOT NULL,
                        the_number_of_goods_purchased BIGINT NOT NULL,
                        sales_amount VARCHAR(100) NOT NULL
                    );""")

        connection.commit()
        print("Success")
    
    except(Exception, Error) as error:
        print("Error", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Closed")
            






def insert_into_statistics_customer(full_name, the_number_of_goods_purchased, sales_amount):
    try:
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'Greate_company')
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO statistics_customer(full_name, the_number_of_goods_purchased, sales_amount)
                       VALUES(%s, %s, %s);""", (full_name, the_number_of_goods_purchased, sales_amount))

        connection.commit()
        print("Success")
    
    except(Exception, Error) as error:
        print("Error", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Closed")
            






def select_statistics_customer():
    try:
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'Greate_company')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM statistics_customer WHERE id = 6 OR full_name ILIKE 'co%';""")

        user = cursor.fetchall()

        return user
    
    except(Exception, Error) as error:
        print("Error", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Closed")

print(select_statistics_customer())
            