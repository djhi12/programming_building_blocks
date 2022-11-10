from csv import list_dialects
import math

print()
print("Welcome to the Shopping Cart Program! \n")

# List
list_items = []
list_items_price = []

action = 0
price = 0
item_remove = ""

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
            print(f"{i + 1}. {list_items[i]} - {list_items_price[i]:.2f}")
            
       

        # Number of items
        print(f"You have {len(list_items)} items in your cart. \n")

    # Remove item
    elif action == 3:
       print()

    # Total items
    elif action == 4:
      
        print()

    print("Please select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit \n")
    action = int(input("Please enter an action: "))
    print()

print("Thank you, for shopping with us! \n")









