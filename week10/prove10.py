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

    # Add item and price
    if action == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))

        list_items.append(item)
        list_items_price.append(price)
        print()
        print(f"'{item}' has been added to the cart")
        print()
        
    # Display items
    elif action == 2:
        print("The contents of the shopping cart are:")
    
        for i in range(len(list_items)):
            
            print(f"{i+1}. {list_items[i]} - ${'%0.2f' % list_items_price[i]}")

        # Number of items
        print(f"You have {len(list_items)} items in your cart. \n")

    # Remove item
    elif action == 3:
        item_remove = int(input("Which item would you like to remove? "))
    
        # list_items.pop(item_remove)
        # # list_items.remove(item_remove)

        # print("Item removed. \n")
        # # Number of items
        # print(f"You have {len(list_items)} items left in your cart. \n")
        
        del list_items[item_remove]
        del list_items_price[item_remove]
        print(f"You removed '{list_items[item_remove]}' from the shopping cart.")
        print(f"You have {len(list_items)} items left in your cart. \n")

    # Total items
    elif action == 4:
        total_price = math.fsum(list_items_price)
        print(f"The total price of the items in the shopping cart is ${format(total_price, '.2f')}")
        print()

    print("Please select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit \n")
    action = int(input("Please enter an action: "))
    print()

print("Thank you, for shopping with us! \n")









