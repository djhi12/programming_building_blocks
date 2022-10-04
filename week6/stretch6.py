print()

# Amusement Park Rides
"""
- No one under 36 inches may ever ride, either by themselves or with another rider.
- Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
- If there are two riders and one of them is at least 18 years old, they may ride together.
"""

# First rider
first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = float(input("What is the height of the first rider? "))
second_rider = input("Is there a second rider (yes/no)? ")

print()

# First person greater than | no
if first_rider_age >= 18 and first_rider_height >= 62 and second_rider.lower() == "no":
    print("Welcome to the ride. Please be safe and have fun! \n")

# First person greater than | yes
elif first_rider_age >= 18 and first_rider_height >= 62 and second_rider.lower() == "yes":
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = float(input("What is the height of the second rider? "))

    print()
    # Second person greater than or equal
    if second_rider_age >= 18 and second_rider_height >= 62:
        print("Welcome to the ride. Please be safe and have fun! \n")

    # Secon person less than
    elif second_rider_age <= 17 and second_rider_height <= 36:
        print("Sorry, you may not ride. \n")

elif first_rider_age >= 12 and first_rider_height >= 52 and second_rider.lower() == "yes":
        print("Welcome to the ride. Please be safe and have fun! \n")

        second_rider_age = int(input("What is the age of the second rider? "))
        second_rider_height = float(input("What is the height of the second rider? "))

        if first_rider_age >= 12 and first_rider_height >= 52 and second_rider_age >= 12 and second_rider_height >= 52:
            print("Welcome to the ride. Please be safe and have fun! \n")

# First person greater than | no
if first_rider_age <= 17 and first_rider_height <= 61 and second_rider.lower() == "no":
    print("Sorry, you may not ride. \n")








# First person lecc than | no
# elif first_rider_age <= 17 and first_rider_height <= 61 and second_rider.lower() == "no":
#     print("Sorry, you may not ride. \n")









