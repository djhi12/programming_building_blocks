from winsound import PlaySound


print()

# Source: https://stackoverflow.com/questions/45362458/capitalize-every-3rd-letter-in-a-string-python

quote = "President Nelson: \"In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.\""

upper_case_letter = list(quote)
# print(upper_case_letter)
# print("".join(upper_case_letter))

num = int(input("Please enter a number: "))
print()

play_again = "yes"

while play_again.lower() == "yes":
    # Double colon (::) is a splicing feature of python (string[start:stop:step]) 
    upper_case_letter[::num] = [letter.upper() for letter in upper_case_letter[::num]]

    quote = "".join(upper_case_letter)

    print(quote)


    play_again = input("Do you want to play again (yes/no)? ")
    print()
    
    num = int(input("Please enter a number: "))
print("Thanks for playing")







# s = "this is a really long string with lots of letters"  

# # convert to list
# a = list(s)

# #change every third letter in place with a list comprehension
# a[3::3] = [x.upper() for x in a[3::3]]

# #back to a string
# s = ''.join(a)

# print(s)

# result: thIsiSarEalLylOngStrIngWitHloTsoFleTteRs

