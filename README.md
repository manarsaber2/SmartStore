# 🛒 Smart Store  

**Smart Store** is a simple Object-Oriented Python project that simulates a digital store where users can browse products, 
add items to a cart, and make purchases using different payment methods.

---

## 📌 Features  
✔️ User Authentication (Login & Role Management)  
✔️ Product Management (Add, Remove, Display)  
✔️ Shopping Cart System  
✔️ Payment Processing (Cash, Card)  
✔️ Data Persistence with `user.json`  

---
## 📌 Concepts Used
✅ Encapsulation → Private attributes in User & Product
✅ Inheritance → CashPayment & CardPayment inherit Payment
✅ Polymorphism → process_payment() works differently in each class
✅ Abstraction → Payment class enforces structure
✅ Exception Handling → Handling stock limits & invalid payments
✅ File Handling → Save user data

## 🚀 How It Works
1️⃣ Displays a menu asking the user for a choice.
2️⃣ Loop continues until the user selects checkout or quit.
3️⃣ Products and cart are managed dynamically.
4️⃣ Handles stock updates when items are added to the cart.
5️⃣ Supports different payment methods (Cash & Card).


## 🔹 Example Run

🔹 Welcome to Smart Store 🔹
1. Login
2. Register
3. Exit
Choose: 2

Enter new username: manar
Enter new password: 1234
✅ Registration successful! Please log in.

1. Login
Username: manar
Password: 1234
✅ Welcome, manar (customer)!

🔹 Store Menu 🔹
1. View Products
2. Add to Cart
3. View Cart
4. Checkout
5. Quit
Enter choice: 1

🛒 Available Products:
1. Laptop | Electronics | $1000 | Stock: 5
2. Phone | Electronics | $500 | Stock: 10
3. Headphones | Accessories | $200 | Stock: 15

Enter choice: 2
Enter product name: Laptop
Enter quantity: 1
✅ Laptop added to cart!

🔹 Store Menu 🔹
1. View Products
2. Add to Cart
3. View Cart
4. Checkout
5. Quit
Enter choice: 3

🛒 Your Cart:
1. Laptop | $1000 | Quantity: 1

🔹 Store Menu 🔹
1. View Products
2. Add to Cart
3. View Cart
4. Checkout
5. Quit
Enter choice: 4

💳 Select Payment Method (cash/card): cash
✅ Payment Successful!

🛒 Thank you for shopping with us!




