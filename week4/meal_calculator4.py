print()

# Meal Calculator
drinks_num = float(input("How many softdrinks? "))
drinks_price = float(input("Softdrink's Price: "))
child_meal = float(input("What is the child's meal price? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children_num = int(input("How many children are there? "))
adult_num = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

# Multiply the child's meal and children number
child_total_amount = child_meal * children_num

# Multiply the adult's meal and adult's number
adult_total_amount = adult_meal * adult_num

# Drinks total
drinks_total = drinks_num * drinks_price

# Children and adult total amount
subtotal = child_total_amount + adult_total_amount + drinks_total

# Sales tax
sales_tax = subtotal * tax_rate / 100

# Total
total = subtotal + sales_tax

print()

# Subtotal
print(f"Subtotal: ${subtotal}")

# Sales tax
print(f"Sales Tax: ${round(sales_tax, 2)}")

# Total
print(f"Total: ${round(total, 2)}")

# Payment amount
amount = float(input("What is the payment amount? "))

# Change
change = amount - total

# Display change
print(f"Change: ${round(change, 2)}")

# Tip
tip = float(input("How much is the tip? "))

# Remaining change
amount_remaining = change - tip

print(f"Remaining change: ${round(amount_remaining, 2)} \n")

# Thank you message
print("Waiter: Thank you, sir, for dining in. Come back again! \n")

