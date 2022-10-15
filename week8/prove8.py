print()

print("Welcome to the word guessing game!")
word = "wilderness"
print()

# print("Your hint is: ")
# for i, letter in enumerate(word):
#         print(letter, end="")

# print()
keep_playing = "yes"

# As long as they say "yes" we will keep playing
while keep_playing == "yes":
    print("Your hint is: ")
    for i, letter in enumerate(word):
        # print(letter, end="")
        hint = letter.replace(letter, "_")
        print(hint, end="")

    # this variable will keep track of how many guesses it took
    guess_count = 0

    guess = -1

    # Keep going as long as the guess doesn't match the magic number
    while guess != word:
        print()
        guess = input("What is your guess? ")
        guess_count = guess_count + 1

        for j, guess1 in enumerate(guess):
            print(end="")

        # if guess != word:
        #     print("Your guess was not correct. \n")
        # else:
        #     print("You guessed it! \n")

        if len(guess) != len(word):
            print("Sorry, the guess must have the same number of letters as the ")
        elif len(guess) == len(word) and guess != word:
            print("Your guess was not correct.")
            print("Your hint is: ")

            for i, letter in enumerate(word):
            # print(letter, end="")
                hint = letter.replace(letter, "_")
                print(hint, end="")
                
        else:
            print("Congratulations! You guessed it!")

    # At this point, they have guessed it correctly
    print(f"It took you {guess_count} guesses")
    print()

    keep_playing = input("Would you like to play again (yes/no)? ")

print("Thank you for playing. Goodbye. \n")