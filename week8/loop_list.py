items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]
for item in items:
    print(f"The item is: {item}")

print()


# -------------------------------

# This loop will start with 100, and go up to, but not including 200
for i in range(100, 105):
    print(i)

# This loop will do the same thing, but this time, it will count by 10's
for i in range(100, 200, 10):
    print(i)

print()



# -----------------------------

first_name = "Brigham"
for letter in first_name:
    print(f"The letter is: {letter}")


# -----------------------------

first_name = "Brigham"

fourth_letter = first_name[3] # Notice, using 3 instead of 4
print(fourth_letter) # outputs a 'g' on the screen



#------------------------------

word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index}Letter: {letter}")
