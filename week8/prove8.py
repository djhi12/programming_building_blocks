from winsound import PlaySound


print()
# Secret word
word = "wilderness"

print("Your hint is: ", end="")

# Iterate the secret word
for letter in word:
    print("_ ", end="")
print()

# Guessing word
# guess = input("What is your guess? ")

# Incrementing score
guess_count = 1

# Play again 
play_again = "yes"

while play_again.lower() == "yes":
    guess = input("What is your guess? ")
    while guess != word:
        guess_length = len(guess)
        word_length = len(word)

        # if guess_length >= word_length:
        #     print("Sorry, the guess must have the same number of letters as the ")

        # elif guess_length >= word_length:
        #     print("Sorry, the guess must have the same number of letters as the ")

        for i in range(guess_length):
            letter = guess[i]

            if letter == word[i]:
                print(f"{letter.upper()}", end="")

                # if len(letter) != len(word[i]):
                #     print("Sorry, the guess must have the same number of letters as the ")

            elif letter in word:
                print(f"{letter.lower()}", end="")
                # print(len(letter))

            # elif len(guess) <= len(word):
            #     print("Sorry, the guess must have the same number of letters as the ")
        
            # elif len(guess) >= len(word):
            #     print("Sorry, the guess must have the same number of letters as the ")

        guess = input("What is your guess? ")
        guess_count += 1

    print(f"You guessed it in {guess_count} guesses!")

    play_again = input("Do you want to play again (yes/no)? ")
    # guess = input("What is your guess? ")

print("Thanks for playing!")
