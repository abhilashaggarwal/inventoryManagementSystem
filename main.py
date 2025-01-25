import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='product_inventory'
)

cursor = conn.cursor()
print("Connected to the database")


class Product:
    def __init__(self,product_name, brand, price, stock, category):
        self.product_name=product_name
        self.brand=brand
        self.price=price
        self.stock=stock
        self.category=category


    def add_product(product_name,brand, price, stock,category):
        query = "INSERT INTO product_inventory (product_name, category, brand, price, stock) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (product_name, category, brand, price, stock))
        conn.commit()
        print("Product added successfully!")

    def delete_product(product_name,brand):
        query = "DELETE FROM product_inventory where (product_name, brand) VALUES (%s, %s)"
        cursor.execute(query, (product_name, brand))
        conn.commit()
        print("Product deleted successfully!")
    
    def update_stock(product_name,brand,stock):
        query = "UPDATE product_inventory SET stock=%s where product_name=%s && brand=%s"
        cursor.execute(query, (stock, product_name, brand))
        conn.commit()
        print(f"Stock updated for {product_name} of {brand} brand successfully!")
    
    def update_price(product_name,brand,price):
        query = "UPDATE product_inventory SET price=%s where product_name=%s && brand=%s"
        cursor.execute(query, (price, product_name, brand))
        conn.commit()
        print(f"Price updated for {product_name} of {brand} brand successfully!")

    def generate_report(category,brand,product_name):
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
                df_category = pd.read_sql(query, conn, params=(category,))
                print(df_category)
            case 2:
                query = "SELECT * FROM product_inventory where brand=%s"
                df_brand = pd.read_sql(query, conn, params=(brand,))
                print(df_brand)
            case 3:
                query = "SELECT * FROM product_inventory where product_name=%s"
                df_product = pd.read_sql(query, conn,params=(product_name,))
                print(df_product)


    def menu(self):
        print("1. Add Product")
        print("2. Delete Product")
        print("3. Update Stock")
        print("4. Update Price")
        print("5. Generate Report")
        value=int(input("Enter Value(1-5):"))
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
                self.add_product()
            case 2:
                self.delete_product()
            case 3:
                self.update_stock()
            case 4:
                self.update_price()
            case 5:
                self.generate_report()

        

        