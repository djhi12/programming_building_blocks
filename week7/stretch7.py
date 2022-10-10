print()
# Team Activity | Guess My Number Game
print("Welcome to guessing number game! Choose between 1 - 10 \n")

# from ast import Num
import random

number = random.randint(1, 10)
# number = 6
print(number)

# Variable on numbers
magic_num = int(input("What is the magic number? "))
guess_num = int(input("What is your guess? "))

attempt = 0

# Loop the question
while magic_num != number:
    # Increment by 1
    attempt += 1
    if guess_num <= number:

        print()

        print("Higher")

        print()

        magic_num = int(input("What is the magic number? "))
        guess_num = int(input("What is your guess? "))

    elif guess_num >= magic_num:

        print()

        print("Lower")
    
        print()

        magic_num = int(input("What is the magic number? "))
        guess_num = int(input("What is your guess? "))

    elif guess_num == magic_num:
        print()

    else:
        print("Type the number according to range.")
   

print(f"You guessed it right! \nNumber of attempts: {attempt} \n")



















#  # Continue
# play_again = input("Do you want to play again? ")

# if play_again.lower() != "no":
#     # Variable on numbers
#     magic_num = int(input("What is the magic number? "))
#     guess_num = int(input("What is your guess? "))
#     print(number)

#     attempt = 0

#     # Loop the question
#     while magic_num != number:
#         # Increment by 1
#         attempt += 1
#         if guess_num <= number:

#             print()

#             print("Higher")

#             print()

#             magic_num = int(input("What is the magic number? "))
#             guess_num = int(input("What is your guess? "))

#         elif guess_num >= magic_num:

#             print()

#             print("Lower")
    
#             print()

#             magic_num = int(input("What is the magic number? "))
#             guess_num = int(input("What is your guess? "))

#         elif guess_num == magic_num:
#             print()

#         else:
#             print("Type the number according to range.")
   
#     print(f"You guessed it right! \nNumber of attempts: {attempt} \n")

# else:
#     print("Thank you for playing!")

        

