from product import Product
from sales import turnOver

def main_menu():
    product_manager = Product()
    sales_manager = turnOver()

    while True:
        print("\n===== Inventory Management System =====")
        print("1. Manage Products")
        print("2. Manage Sales")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")
        if choice == "1":
            product_manager.menu()  # Implement menu in product.py
        elif choice == "2":
            sales_manager.menu()  # Implement menu in sales.py
        elif choice == "3":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()