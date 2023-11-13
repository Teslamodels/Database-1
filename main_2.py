from statistics_customer import create_table_statistics_customer, insert_into_statistics_customer


full_name = input("Full name: ")
the_number_of_goods_purchased = int(input("The number of goods purchased: "))
sales_amount = input("Sales amount: ")

insert_into_statistics_customer(full_name=full_name, the_number_of_goods_purchased=the_number_of_goods_purchased, sales_amount=sales_amount)

print(create_table_statistics_customer())