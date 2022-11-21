print()

# Square area
# A = a ** 2
def compute_area_square(side):
    square_area = side * side
    return square_area

# Rectangle area
# A = width * length
def compute_area_rectangle(width, length):
    rectangle_area = width * length
    return rectangle_area

# Circle area
# Area = pi * r ** 2
# Radius = Cicumference / 2 * radius
# pi = 3.14159
def compute_area_circle(radius, pi):
    circumference = float(input("Type the circuference: "))
    circle_area = pi * radius ** 2
    
    