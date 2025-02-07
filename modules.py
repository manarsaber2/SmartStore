import json

# ✅ User Management
class User:
    users = []  # Store registered users

    def __init__(self, username, password, role="customer"):
        self.__username = username
        self.__password = password
        self.role = role
        User.users.append(self)

    @classmethod
    def authenticate(cls, username, password):
        for user in cls.users:
            if user.__username == username and user.__password == password:
                return user
        return None

    @classmethod
    def save_users(cls):
        data = [{"username": user.__username, "password": user.__password, "role": user.role} for user in cls.users]
        with open("users.json", "w") as file:
            json.dump(data, file)

    @classmethod
    def load_users(cls):
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
                for user in data:
                    cls(user["username"], user["password"], user["role"])
        except FileNotFoundError:
            pass


# ✅ Product Class
class Product:
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} | {self.category} | ${self.price} | Stock: {self.stock}"


# ✅ Store Class
class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("\n🛒 Available Products:")
        for idx, product in enumerate(self.products, 1):
            print(f"{idx}. {product}")
        print()


# ✅ Cart Class
class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
            print(f"✅ {quantity}x {product.name} added to cart!\n")
        else:
            print(f"❌ Not enough stock for {product.name}!\n")

    def view_cart(self):
        if not self.items:
            print("\n🛒 Your cart is empty!\n")
        else:
            print("\n🛒 Your Cart:")
            total = 0
            for product, quantity in self.items:
                print(f"{quantity}x {product.name} - ${product.price * quantity}")
                total += product.price * quantity
            print(f"💰 Total: ${total}\n")


# ✅ Payment Classes
class Payment:
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"💵 Cash Payment of ${amount} processed successfully!\n")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"💳 Card Payment of ${amount} processed successfully!\n")
