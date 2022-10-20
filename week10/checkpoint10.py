print()

list_items = []

item = ""

# List the items
while item.lower() != "quit":
 
    item = input("Please enter the items of the shopping list (type: quit to finish): ")
    print(f"item: {item}")
    list_items.append(item)
    print()

print("The shopping list is: ")

# Iterate items
for list_item in list_items:
    print(list_item)

print()
# Indexes using enumerate
print("The shopping list with indexes is:")
for i, list_item in enumerate(list_items):
    print(f"{i}. {list_item}")
print()

# Change item
for i, list_item in enumerate(list_items):
    change_item = ""
    if i == change_item:
        print("Hello")
        # list_items.pop(i)
        # list_items.append(new_item)
    change_item = int(input("Which item would you like to change? "))
    # new_item = input("What is the new item?")
print()

# print("The shopping list with indexes is:")
# for i, list_item in enumerate(list_items):
#     print(f"{i}. {list_item}")


