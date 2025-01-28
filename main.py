import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='inventorymanagementsystem'
)

print("Connected to the database")


class Product:
    def __init__(self):
        self.conn = conn
        self.cursor = conn.cursor()


    def add_product(self,product_name,brand, price, stock,category):
        query = "INSERT INTO product_inventory (product_name, category, brand, price, stock) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (product_name, category, brand, price, stock))
        self.conn.commit()
        print("Product added successfully!")

    def delete_product(self,product_name,brand):
        query = "DELETE FROM product_inventory where product_name=%s AND brand=%s"
        self.cursor.execute(query, (product_name, brand))
        self.conn.commit()
        print("Product deleted successfully!")
    
    def update_stock(self,product_name,brand,stock):
        query = "UPDATE product_inventory SET stock=%s where product_name=%s && brand=%s"
        self.cursor.execute(query, (stock, product_name, brand))
        self.conn.commit()
        print(f"Stock updated for {product_name} of {brand} brand successfully!")
    
    def update_price(self,product_name,brand,price):
        query = "UPDATE product_inventory SET price=%s where product_name=%s && brand=%s"
        self.cursor.execute(query, (price, product_name, brand))
        self.conn.commit()
        print(f"Price updated for {product_name} of {brand} brand successfully!")

    def generate_report(self,category,brand,product_name):

            print("1. Based on Category")
            print("2. Based on Brand")
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
                    query = "SELECT * FROM product_inventory where category=%s"
                    df_category = pd.read_sql(query, self.conn, params=(category,))
                    print(df_category)
                case 2:
                    query = "SELECT * FROM product_inventory where brand=%s"
                    df_brand = pd.read_sql(query, self.conn, params=(brand,))
                    print(df_brand)
                case 3:
                    query = "SELECT * FROM product_inventory where product_name=%s"
                    df_product = pd.read_sql(query, self.conn,params=(product_name,))
                    print(df_product)


    def menu(self):
        while True:
            print("1. Add Product")
            print("2. Delete Product")
            print("3. Update Stock")
            print("4. Update Price")
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
                    product_name = input("Enter product name: ")
                    brand = input("Enter brand: ")
                    price = float(input("Enter price: "))
                    stock = int(input("Enter stock: "))
                    category = input("Enter category: ")
                    self.add_product(product_name, brand, price, stock, category)
                case 2:
                    product_name = input("Enter product name to delete: ")
                    brand = input("Enter brand: ")
                    self.delete_product(product_name, brand)
                case 3:
                    product_name = input("Enter product name: ")
                    brand = input("Enter brand: ")
                    stock = int(input("Enter new stock: "))
                    self.update_stock(product_name, brand, stock)
                case 4:
                    product_name = input("Enter product name: ")
                    brand = input("Enter brand: ")
                    price = float(input("Enter new price: "))
                    self.update_price(product_name, brand, price)
                case 5:
                    category = input("Enter category (or leave blank): ") or None
                    brand = input("Enter brand (or leave blank): ") or None
                    product_name = input("Enter product name (or leave blank): ") or None
                    self.generate_report(category, brand, product_name)
                case 6:
                    print("Exiting the program. Goodbye!")
                    break

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("Database connection closed.")

p1=Product()
p1.menu()