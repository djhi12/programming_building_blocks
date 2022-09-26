print()

# Grade Calculator
"""
 A >= 90
 B >= 80
 C >= 70
 D >= 60
 F < 60
"""
grade_percentage = int(input("Type the grade percentage: "))

sign = grade_percentage % 10

if grade_percentage >= 90:
    if sign < 3:
        print("A-")
    else:
        print("A")
elif grade_percentage >= 80:
    if sign < 3:
        print("B-")
    else:
        print("B")
elif grade_percentage >= 70:
    if sign < 3:
        print("C-")
    else:
        print("C")
elif grade_percentage >= 60:
    if sign < 3:
        print("D-")
    else:
        print("D")
else:
    print("F")



