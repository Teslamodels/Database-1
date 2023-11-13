from statistics_employes import create_table_statistics_employes, insert_into_statistics_employes


full_name = input("Full name: ")
num_customers = int(input("Number customers: "))
num_products = int(input("Number products: "))
trade_amount = input("Trade amount: ")

insert_into_statistics_employes(full_name=full_name, num_customers=num_customers, num_products=num_products, trade_amount=trade_amount)



print(create_table_statistics_employes())