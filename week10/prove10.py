from csv import list_dialects
import math

print()
print("Welcome to the Shopping Cart Program! \n")

# List
list_items = []
list_items_price = []

action = None
price = None
item_remove = None

while action != 5:

    if action == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))

        list_items.append(item)
        list_items_price.append(price)
        print()
        print(f"'{item}' has been added to the cart")
        print()
        

    elif action == 2:
        print("The contents of the shopping cart are:")
        # for list_item in list_items:
        #     print(list_item)
        for i in range(len(list_items)):
            print(f"{i}. {list_items[i]} - ${list_items_price[i]}")
        print()

    elif action == 3:
        item_remove = int(input("Which item would you like to remove? "))
        # for list_item_remove in list_items:
        #     if item_remove == list_item_remove:
        #         list_items.remove(item_remove)
        list_items.pop(item_remove)

        print("Item removed.")
        print()

    elif action == 4:
        total_price = math.fsum(list_items_price)
        print(f"The total price of the items in the shopping cart is ${total_price}")
        print()
    else:
        print("Please type the correct number.")

    print("Please select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit \n")
    action = int(input("Please enter an action: "))
    print()

print("Thank you, for shopping with us!")









