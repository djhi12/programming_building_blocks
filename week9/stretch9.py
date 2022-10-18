print()
from statistics import mean 

# print("Enter a list of numbers, type 0 when finished.")

sum = 0
number = ""
list_of_numbers = []

while number != 0:
    number = int(input("Enter a number: "))

    # Add every number in list
    list_of_numbers.append(number)

for num in list_of_numbers:

    # sum
    sum += num

    # Average
    average_num = mean(list_of_numbers)

    # Largest number
    largest_num = max(list_of_numbers)
    

print(f"The sum is: {sum}")
print(f"The average is: {average_num}")
print(f"The Largest number is: {largest_num}")


