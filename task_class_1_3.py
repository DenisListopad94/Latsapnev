''''
3.	Реализуйте класс Shop. 
Предусмотреть возможность работы с произвольным числом продуктов, поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"Product '{name}' added to the shop.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product '{name}' removed from the shop.")
                return
        print(f"Product '{name}' not found in the shop.")

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def display_products(self):
        if not self.products:
            print("The shop is empty.")
        else:
            print("Products in the shop:")
            for product in self.products:
                print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

shop = Shop()

shop.add_product("Apple", 1.5, 10)
shop.add_product("Banana", 0.8, 15)
shop.add_product("Orange", 2.0, 8)

shop.display_products()

product_to_find = "Banana"
found_product = shop.find_product(product_to_find)
if found_product:
    print(f"{product_to_find} found in the shop.")
else:
    print(f"{product_to_find} not found in the shop.")

shop.remove_product("Banana")
shop.display_products()