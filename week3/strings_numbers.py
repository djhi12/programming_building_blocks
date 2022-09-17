# apple_count = 5

# Error on this line... You can't add strings and integers together!
# print("You have "+ apple_count + " apples") # ERROR!

# -----------------

# This creates a new integer variable with the value of 10 
# There is nothing magical about the "_num" in the variable name, it will just
# help us keep track of it
length_num = 50
width_num = 10

# If you add the numbers together, you would get the result you expect:
print(length_num + width_num) # This displays: 60

# You can convert the values to the strings "50" and "10" like this:
length_string = str(length_num)
width_string = str(width_num)

# The computer now thinks of these variable as two characters, the digit 5 followed
# by the digit 0, and the digit 1 followed by the digit 0.

# If you try to add the two strings together, it will concatenate them, or display
# one after the other:
print(length_string + width_string) # This displays: 5010



# ----------------

quantity_from_user = input("How many items do you have? ")

# The variable quantity_from_user is a string.
# To convert it to an integer you use the int(...) notation:
quantity_number = int(quantity_from_user)

# Because the quantity_number variable is an integer you can do math with it:
double_number = quantity_number * 2

# If you want to use these values in strings, you CANNOT just add them, you first
# have to convert them to a string:

# WRONG:
# print("Twice as many is: "+ double_number)

# Right:
double_string = str(double_number)
print("Twice as many is: "+ double_string)

# You can also do this in one step:
# Right:
print("Twice as many is "+ str(double_number))



# ---------------

# Using two lines:
people_string = input("How many people are in the room? ")
people_number = int(people_string)

# Using one line:
people_number = int(input("How many people are in the room? "))

# The same works for floating point numbers:
length_number = float(input("What is the length? "))

