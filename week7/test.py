print()
# https://www.youtube.com/watch?v=cNMleaCIIXQ

# # Word guessing game
# print("Welcome to the word guessing game! \n")

# secret_word = "tower"
# print(secret_word)
# print(len(secret_word)) # 5

# print("Your hint is: _ _ _ _ _")
# guess = input("What is your guess? ")

# while secret_word != guess:

#     if len(secret_word) >= len(guess):
#         print("Sorry, the guess must have the same number of letters as the secret word.")
#         guess = input("What is your guess? ")

#     elif len(secret_word) <= len(guess):
#         print("Sorry, the guess must have the same number of letters as the secret word.")
#         guess = input("What is your guess? ")

#     elif len(secret_word) == len(guess) and secret_word != guess:
#         print("Your guess was not correct.")
#         guess = input("What is your guess? ")
    
#     break

# print("Congratulations! You guessed it!")

print("Welcome to the word guessing game!")

word = "wilderness"
print(len(word))
print(word)

hint = "_ " * len(word)
print(f"Your hint is: {hint}")

guess = input("What is your guess? ")
index = -2

def letter_position(guess, word, spaces):
    while index != -1:
        if guess in word:
            index = word.find(guess)
            remove = "*"
            word = word[:index] + remove + word[:index + 1:]
            spaces[index] = guess 

        else:
            index = -1

    return(word, spaces)

def win_check(spaces):
    for i in range(0, len(spaces)):
        print()






