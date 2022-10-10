print()
# Team Activity | Guess My Number Game

from ast import Num
import random

# number = random.randint(1, 10)
number = 10
print(number)

# Variable on numbers
magic_num = int(input("What is the magic number? "))
guess_num = int(input("What is your guess? "))

# Loop the question
while True:
    if magic_num == number:
        if guess_num <= magic_num:
            print("Higher")

        elif guess_num >= magic_num:
            print("Lower")
        
        else:
            print("You guessed it!")
    



