print()
# Team Activity | Guess My Number Game

from ast import Num
import random

number = random.randint(1, 10)
# number = 6
# print(number)

# Variable on numbers
magic_num = int(input("What is the magic number? "))
guess_num = int(input("What is your guess? "))

# Loop the question
while magic_num != number:
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

print()

print("You guess it! \n")
