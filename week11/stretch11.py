print()
with open("hr.txt") as details:
    for detail in details:
        parts = detail.split(" ")
        # print(parts)

        name = parts[0]
        title = parts[2]
        id = parts[1]
        salary = parts[3]
        cs

        print(f"{name.strip()} (ID: {id.strip()}), {title.strip()} - ${salary.strip()}")
    print()



