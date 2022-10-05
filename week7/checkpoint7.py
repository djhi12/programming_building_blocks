from turtle import position


print()

# Positive number

positive_num = int(input("Please type a positive number: "))

while positive_num <= 0:
    print("Sorry, that is a negative number. Please try again. \n")
    positive_num = int(input("Please type a positive number: "))

print(f"The number is: {positive_num} \n")