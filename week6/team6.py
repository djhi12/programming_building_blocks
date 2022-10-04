print()

# Amusement Park Rides

# First rider
first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = float(input("What is the height of the first rider? "))
second_rider = input("Is there a second rider (yes/no)? ")

print()

if first_rider_age >= 18 and first_rider_height >= 62 and second_rider.lower() == "no":
    print("Welcome to the ride. Please be safe and have fun! \n")

elif first_rider_age >= 18 and first_rider_height >= 62 and second_rider.lower() == "yes":
    # Second rider
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = float(input("What is the height of the second rider? "))

    print()

    if second_rider_age >= 18 or second_rider_height <= 35:
        print("Sorry, you may not ride. \n")

    elif second_rider_age >= 18 or second_rider_height >= 36:
        print("Welcome to the ride. Please be safe and have fun! \n")

elif first_rider_age <= 17 and first_rider_height <= 61 and second_rider.lower() == "no":
    print("Sorry, you may not ride. \n")

elif first_rider_age <= 17 and first_rider_height <= 61 and second_rider.lower() == "no":
    print("Sorry, you may not ride. \n")








