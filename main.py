from modules import User, Store, Cart, Product, CashPayment, CardPayment
import sys
sys.stdout.reconfigure(encoding="utf-8")

# Load existing users
User.load_users()

# ✅ Register or Login
print("🔹 Welcome to Smart Store 🔹")
while True:
    action = input("1. Login\n2. Register\n3. Exit\nChoose: ")
    
    if action == "1":  # Login
        username = input("Username: ")
        password = input("Password: ")
        user = User.authenticate(username, password)
        
        if user:
            print(f"\n✅ Welcome, {username} ({user.role})!")
            break
        else:
            print("\n❌ Invalid credentials! Try again.\n")

    elif action == "2":  # Register
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        new_user = User(username, password)
        User.save_users()
        print("\n✅ Registration successful! Please log in.\n")

    elif action == "3":  # Exit
        print("\n👋 Goodbye!")
        exit()

    else:
        print("\n❌ Invalid choice! Try again.\n")


# ✅ Store Setup
store = Store()
cart = Cart()

p1 = Product("Laptop", "Electronics", 1000, 5)
p2 = Product("Phone", "Electronics", 500, 10)
p3 = Product("Headphones", "Accessories", 200, 15)

store.add_product(p1)
store.add_product(p2)
store.add_product(p3)

# ✅ Main Menu Loop
while True:
    print("\n🔹 Store Menu 🔹")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Quit")
    
    choice = input("Enter choice: ")

    if choice == "1":  # View products
        store.display_products()

    elif choice == "2":  # Add to cart
        store.display_products()
        try:
            product_index = int(input("Select product number: ")) - 1
            quantity = int(input("Enter quantity: "))
            if 0 <= product_index < len(store.products):
                cart.add_to_cart(store.products[product_index], quantity)
            else:
                print("\n❌ Invalid product selection!\n")
        except ValueError:
            print("\n❌ Enter valid numbers!\n")

    elif choice == "3":  # View cart
        cart.view_cart()

    elif choice == "4":  # Checkout
        cart.view_cart()
        if cart.items:
            payment_type = input("Payment method (cash/card): ").lower()
            total_amount = sum(p.price * q for p, q in cart.items)

            if payment_type == "cash":
                payment = CashPayment()
            elif payment_type == "card":
                payment = CardPayment()
            else:
                print("\n❌ Invalid payment method!\n")
                continue

            payment.process_payment(total_amount)
            print("\n✅ Purchase completed! Thank you for shopping!\n")
            break  # End shopping

    elif choice == "5":  # Quit
        print("\n👋 Goodbye!")
        break

    else:
        print("\n❌ Invalid choice! Try again.\n")
