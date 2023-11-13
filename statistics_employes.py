import psycopg2
from psycopg2 import Error


def create_table_statistics_employes():
    try:
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'Greate_company')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE statistics_employes(
                       ID SERIAL PRIMARY KEY,
                       full_name VARCHAR(1000) NOT NULL,
                       num_customers BIGINT NOT NULL,
                       num_products BIGINT NOT NULL,
                       trade_amount VARCHAR(100) NOT NULL
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
            






def insert_into_statistics_employes(full_name, num_customers, num_products, trade_amount):
    try:
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'Greate_company')
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO statistics_employes(full_name, num_customers, num_products, trade_amount)
                       VALUES(%s, %s, %s, %s);""", (full_name, num_customers, num_products, trade_amount))

        connection.commit()
        print("Success")
    
    except(Exception, Error) as error:
        print("Error", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Closed")
            






def select_statistics_employes():
    try:
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'Greate_company')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM statistics_employes;""")

        user = cursor.fetchall()

        return user
    
    except(Exception, Error) as error:
        print("Error", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Closed")

print(select_statistics_employes())
            