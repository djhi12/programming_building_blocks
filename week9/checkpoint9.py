print()

# 09 Prepare: Checkpoint


name = ""
names = []
while name != "end":
    name = input("Type the name of a friend: ")

    names.append(name)
    # names.pop()
    remove_name = names[:-1]
for list_name in remove_name:
    print(list_name)
    # name = input("Type the name of a friend: ")
