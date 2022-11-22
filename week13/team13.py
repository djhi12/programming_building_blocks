print()

shape_type = ""

while shape_type.lower() != "quit":
  
    if shape_type.lower() == "square":
        # Square area
        # A = a ** 2
        def compute_area_square(side):
            square_area = side * side
            return square_area

        side = float(input("Type the side of a square: "))
        print(compute_area_square(side))
        print()
        
    elif shape_type.lower() == "rectangle":
        # Rectangle area
        # A = width * length    
        def compute_area_rectangle(width, length):
            rectangle_area = width * length
            return rectangle_area

        width = float(input("Type the width: "))
        length = float(input("Type the length: "))
        print(compute_area_rectangle(width, length))
        print()
        
    elif shape_type.lower() == "circle":
        # Circle area
        # Area = pi * r ** 2
        # Radius = Cicumference / 2 * pi
        pi = 3.14159
        def compute_area_circle(radius, pi):
            circle_area = pi * radius ** 2
            return circle_area
    
        circumference = float(input("Type the circumference: "))  
        radius = circumference / 2 *  pi
        print(compute_area_circle(radius, pi))
        print()
    
    shape_type = input("Type the shape for calculation: SQUARE, RECTANGLE, CIRCLE. If you want to end, just type QUIT: ")
    
print("Have a nice day! \n")
    