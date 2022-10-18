print()

# 09 Prepare: Checkpoint


name = ""
print()
names = []
while name != "end":
    name = input("Type the name of a friend: ")
    names.append(name)

    # Create a variable and remove the last word using [:-1]
    remove_name = names[:-1]

    # Iteration
for list_name in remove_name:
    print(list_name)
    # name = input("Type the name of a friend: ")

print()