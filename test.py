# Grade Calculator
"""
 A >= 90 # Excellent!
 B >= 80 # You passed!
 C >= 70 # Good job!
 D >= 60 # Study more!
 F < 60 # Better luck nextime!
"""
from signal import signal


letter = ""

grade = int(input("Type your grade: "))
sign = grade % 10

print(sign)

if grade >= 90:

    letter = "A"

elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"{letter}")



    
