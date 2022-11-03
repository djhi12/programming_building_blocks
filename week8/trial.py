word = "dog"

guess = input("What is your guess? ")

for i in range(len(word)):
    letter_word = word[i]
    letter_guess = guess[i]
    
    if letter_word == letter_guess:
        print(letter_guess.upper(), end="")
        
    else:
        print(letter_guess.replace(letter_guess, " _"), end="")