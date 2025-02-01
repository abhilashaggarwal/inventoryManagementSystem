import pandas as pd
from database_connect import engine, db_connection

class Sales:
    def __init__(self):
        self.conn = db_connection
        self.cursor = self.conn.cursor()


    def add_sales(self,product_name, quantity, date, sales_price, customer_name):
        query = "INSERT INTO sales_inventory (product_name, quantity, date, sales_price, customer_name) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (product_name, quantity, date, sales_price, customer_name))
        self.conn.commit()
        print("Sale data added successfully!")

    def delete_sales(self, product_name, date, customer_name):
        query = "DELETE FROM sales_inventory where product_name=%s AND date=%s AND customer_name=%s"
        self.cursor.execute(query, (product_name, date, customer_name))
        self.conn.commit()
        print("Product deleted successfully!")
    
    def update_quantity(self,quantity, customer_name, date):
        query = "UPDATE sales_inventory SET quantity=%s where customer_name=%s AND date=%s"
        self.cursor.execute(query, (quantity, customer_name, date))
        self.conn.commit()
        print(f"Sales inventory for {customer_name} updated successfully!")
    
    def update_price(self, customer_name, date, price):
        query = "UPDATE sales_inventory SET price=%s where customer_name=%s AND date=%s"
        self.cursor.execute(query, (price, customer_name, date))
        self.conn.commit()
        print(f"Price updation for {customer_name} successfully!")

    def generate_report(self,customer_name,date1,date2,product_name): 

            print("1. Based on Date Range")
            print("2. Based on Customer Name")
            print("3. Based on Product Name")
            while True:
                try:
                    value = int(input("Enter Value (1-3): "))
                    if value not in [1, 2, 3]:
                        raise ValueError("Invalid input")
                    break  # If the value is valid, exit the loop
                except ValueError:
                    print("Please enter a valid input from 1-3")

            match value:
                case 1:
                    query = "SELECT * FROM sales_inventory where date1 > %s AND date2 < %s"
                    df_dateRange = pd.read_sql(query, engine, self.conn, params=(date1,date2))
                    print(df_dateRange)
                case 2:
                    query = "SELECT * FROM sales_inventory where customer_name=%s"
                    df_brand = pd.read_sql(query, engine, self.conn, params=(customer_name,))
                    print(df_brand)
                case 3:
                    query = "SELECT * FROM sales_inventory where product_name=%s"
                    df_product = pd.read_sql(query, engine, self.conn,params=(product_name,))
                    print(df_product)


    def menu(self):
        while True:
            print("1. Add Sales Data")
            print("2. Remove Sales Data")
            print("3. Update Quantity")
            print("4. Update Pricing")
            print("5. Generate Report")
            print("6. Exit")
        
            while True:
                try:
                    value = int(input("Enter Value (1-6): "))
                    if value not in range(1,7):
                        raise ValueError("Invalid input")
                    break  # If the value is valid, exit the loop
                except ValueError:
                    print("Please enter a valid input from 1-6")
            match value:
                case 1:
                    product_name = input("Enter Product Name: ")   #product_name, quantity, date, sales_price, customer_name
                    quantity = input("Enter Quantity: ")
                    date = input("Enter Date: ")
                    sales_price = int(input("Enter Sales Price of product: "))
                    customer_name = input("Enter Customer Name: ")
                    self.add_product(product_name, quantity, date, sales_price, customer_name)
                case 2:
                    product_name = input("Enter product name to delete: ")
                    date = input("Enter Date: ")
                    customer_name = input("Enter Customer Name: ")
                    self.delete_product(product_name, date, customer_name)
                case 3:
                    quantity = input("Enter Quantity: ")
                    date = input("Enter Date: ")
                    customer_name = input("Enter Customer Name: ")
                    self.update_stock(customer_name, date, quantity)
                case 4:
                    date = input("Enter Date: ")
                    customer_name = input("Enter Customer Name: ")
                    price = float(input("Enter new price: "))
                    self.update_price(customer_name, date, price)
                case 5:
                    product_name = input("Enter Product name (or leave blank): ") or None
                    date1 = input("Enter Date1: ")
                    date2 = input("Enter Date2: ")
                    customer_name = input("Enter Customer name (or leave blank): ") or None
                    self.generate_report(product_name, date1, date2, customer_name)
                case 6:
                    print("Exiting the program. Goodbye!")
                    break

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("Database connection closed.")
