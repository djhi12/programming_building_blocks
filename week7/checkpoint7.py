print()

# Positive number

positive_num = int(input("Please type a positive number: "))

print()

while positive_num <= 0:
    print("Sorry, that is a negative number. Please try again. \n")
    positive_num = int(input("Please type a positive number: "))

print()

print(f"The number is: {positive_num} \n")


# Candy

candy = input("May I have a piece of candy? ")

print()

while candy.lower() == "no":
    print("No")
    candy = input("May I have a piece of candy? ")

print("Thank you! \n")

