print()
print("Welcome to the word guessing game! \n")

name = "daniel"
print("Your hint is: ", end="")
for letter_name in name:
    hint = letter_name.replace(letter_name, "_")
    print(hint, end="")

print()
guess = input("What is your guess? ")

if letter_name == guess:
    print("Awesome!")

    

    
