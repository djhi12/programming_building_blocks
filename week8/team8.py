print()

word = "Commitment"

fav_letter = input("What is your favorite letter? ")

for letter in word:
    # print(letter)

    if letter == fav_letter.lower():
        print(letter.replace(fav_letter, "_"), end=" ")
        

    else:
        print(letter.lower(), end=" ")

print()