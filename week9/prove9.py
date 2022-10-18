from csv import list_dialects


print()
print("Welcome to the Shopping Cart Program! \n")

# List
list_items = []
list_items_price = []

action = ""

while action != 5:
    # action = int(input("Please enter an action: "))

    if action == 1:
        item = input("What item would you like to add? ")

        list_items.append(item)
        print()
        print(f"'{item}' has been added to the cart")
        print()
        # action = int(input("Please enter an action: "))

    elif action == 2:
        print("The contents of the shopping cart are:")
        for list_item in list_items:
            print(list_item)
        print()
    
    elif action == 3:
        print()

    elif action == 4:
        print()

    else:
        print("Please enter action from 1, 2, and 5.")
        print()

    print("Please select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit \n")
    action = int(input("Please enter an action: "))
    print()

print("Thank you, for shopping with us!")









