print()

# Lists
bank_names = []
bank_balances = []

# Ask the user
name = ""
balance = 0
print("Enter the names and balances of bank accounts (type: quit when done) \n")

while name.lower() != "quit":
    # Bank Details
    name = input("What is the name of this account? ")
    bank_names.append(name)

    balance = float(input("What is the balance? "))
    bank_balances.append(balance)
    print()

print("Account Information:")
for bank_name in bank_names:
    bank_balance = bank_balances[bank_name]
    print(f"{bank_name} - {bank_balance}")
