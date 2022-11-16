print()

print("Welcome to the shopping cart program!")

# List
list_items = []
list_items_price = []

action = ""

while action != 5:
    
    if action == 1:
        item = input("What item would like to add? ")
        
        list_items.append(item) # Add item
        print(f"'{item}' has been added to the cart.")
        
    elif action == 2:
        print("The contents of the shopping cart are:")
        
        for list_item in list_items:
            print(list_item)
            
    elif action == 3:
        print()
        
        
    elif action == 4:
        print()
    
    action = int(input("Please enter an action: "))
    
print("Thank you shopping with us!")

