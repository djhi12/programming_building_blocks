print()
with open("hr.txt") as details:
    for detail in details:
        parts = detail.split(" ")
        # print(parts)

        name = parts[0]
        title = parts[2]

        print(f"Name: {name.strip()}, Title: {title.strip()}")
    print()



