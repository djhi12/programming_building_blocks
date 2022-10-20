print()

# Lists
bank_names = []
bank_balances = []

# Ask the user
name = ""
balance = "d"
print("Enter the names and balances of bank accounts (type: quit when done) \n")
while name.lower != "quit":

    # Bank Details
    name = input("What is the name of this account? ")
    bank_names.append(name)

    balance = float(input("What is the balance? "))
    bank_balances.append(balance)

print("Account Information:")

