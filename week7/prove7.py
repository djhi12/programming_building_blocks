print()
word = "wilderness"

keep_playing = "yes"

# As long as they say "yes" we will keep playing
while keep_playing == "yes":

    # this variable will keep track of how many guesses it took
    guess_count = 0

    guess = -1

    # Keep going as long as the guess doesn't match the magic number
    while guess != word:
        guess = input("What is your guess? ")
        guess_count = guess_count + 1

        if guess != word:
            print("Your guess was not correct. \n")
        else:
            print("You guessed it! \n")

    # At this point, they have guessed it correctly
    print(f"It took you {guess_count} guesses")
    print()

    keep_playing = input("Would you like to play again (yes/no)? ")

print("Thank you for playing. Goodbye. \n")




# secret_word = "lehi"
# guess = None
# attempts = 0

# while secret_word != guess:
#     attempts += 1
#     guess = input("What is your guess? ")

#     if secret_word != guess:
#         print("Try again")
#     else:
#         print(f"You guessed it right! Total number of guessed is {attempts} \n")



















