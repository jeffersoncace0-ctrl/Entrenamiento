📦 Inventory Management
A Python console program that manages product inventory, validating numeric inputs and calculating the total cost per product.
📋 Description:
The program guides the user to enter the name, price, and quantity of a product. It validates that the price and quantity are numeric values greater than zero using loops with exception handling. Finally, it calculates the total cost and displays a formatted summary.
⚙️ Requirements:
Python 3.x


No external libraries are required.
🚀 Usage:
Run the script from the terminal:
python inventario.py
The program will interactively request the following information:
Field
Type
Description
Name
Text
Product name
Price
Decimal
Unit price of the product
Quantity
Integer
Number of units

💡 Example Execution:
Enter the product name: Rice
Enter the product price: $2.500
Enter the product quantity: 4

Product: Rice | Price: $2.500 | Quantity: 4 | Total: $10.000
🔒 Data Validation:
The program applies two independent validations, one for the price and another for the quantity. Each checks two conditions:
1️⃣ The entered value must be numeric.
 If it is not numeric, an error message appears and the program asks again:
Enter the product price: $abc
Error: Enter numeric values only
Enter the product price: $
2️⃣ The value must be greater than zero.
 If it is zero or negative, an error message appears and the program asks again:
Enter the product price: $-5
Error: Enter a valid value.
Enter the product price: $
The loop repeats until valid values are entered in both fields.
🧠 Program Logic:
Ask for the product name


Repeat until a valid price is obtained:
 a. Request price (float)
 b. If not numeric → show error and retry
 c. If less than or equal to zero → show error and retry


Repeat until a valid quantity is obtained:
 a. Request quantity (int)
 b. If not numeric → show error and retry
 c. If less than or equal to zero → show error and retry


Calculate: total_cost = price × quantity


Display the formatted summary


📁 Project Structure:
project/
├── docs/
│   └── diagramagestioninventario.png  # Program flowchart
├── .gitignore
├── inventario.py                      # Main script
├── LICENSE
└── README.md

👤 Author: 
Jefferson Cacerez


