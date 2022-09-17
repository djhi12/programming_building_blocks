print()

# Core Requirements
# Square
# A = s**2 (s is the length of the side of the square.)
square = float(input("what is the length of a side of the square? "))
area = square ** 2
print(f"The area of the square is: {area} \n")


# Rectangle
# A = LW (L and W are the lengths of the rectangle's sides (length and width).)
length = float(input("What is the length of rectangle? "))
width = float(input("What is the width of the rectangle? "))
print(f"The area of the rectangle is: {length * width} \n")


# Circle
# A = 3.14 * r**2
radius = float(input("What is the radius of the circle? "))
print(f"The area of the circle is: {3.14 * radius ** 2} \n")
