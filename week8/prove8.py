print()
print("Welcome to the word guessing game! \n")

# Guessing word
word = "wilderness"
print(len(word))
letter = list(word)
print(letter)

hint = word.replace("wilderness", "_", 9)
print(f"Your hint is: {hint}")


print()