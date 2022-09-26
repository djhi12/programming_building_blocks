# Comparing number
first_num = int(input("What is the first number? "))
second_num = int(input("What is the second number? "))

# Greater
if first_num > second_num:
    print("The first number is greater \n The numbers are not equal \n The second number is not greater \n")

# Less than
elif first_num < second_num:
    print("The first number is not greater \n The numbers are not equal \n The second number is greater \n")

# Equal
elif first_num == second_num:
    print("The first number is not greater \n The numbers are equal \n The second number is not greater \n")

# Comparing Strings
fav_animal = input("What is your favorite animal? ")

if fav_animal.lower() == "bear":
    print("That's my favorite animal too! \n")

else:
    print("That one is not my favorite. \n")
