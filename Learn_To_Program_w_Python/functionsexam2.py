# rhombus, parallagram, trapazoid, triangle

import math

def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "triangle":
        triangle_area()
    elif shape == "rhombus":
        rhombus_area()
    elif shape == "trapezoid":
        trapezoid_area()
    elif shape == "parallelogram":
        parallelogram_area()
    else:
        print("Please enter rectangle, circle, triangle,")
        print("rhombus, trapezoid, or parallelogram")

def rectangle_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    area = length * width

    print("The area of the rectangle is {:.2f}".format(area))

def circle_area():
    radius = float(input("Enter the radius: "))

    area = math.pi * (math.pow(radius, 2))

    print("The area of the circle is {:.2f}".format(area))

def triangle_area():
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))

    area = (base * height) / 2

    print("The area of the triangle is {:.2f}".format(area))

def rhombus_area():
    diag1 = float(input("Enter the first diagonal: "))
    diag2 = float(input("Enter the second diagonal: "))

    area = (diag1 * diag2) / 2

    print("The area of the rhombus is {:.2f}".format(area))

def trapezoid_area():
    base_short = float(input("Enter the short base: "))
    base_long = float(input("Enter the long base: "))
    height = float(input("Enter the height: "))

    area = ((base_short + base_long) / 2) * height

    print("The area of the trapezoid is {:.2f}".format(area))

def parallelogram_area():
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))

    area = base * height

    print("The area of the parallelogram is {:.2f}".format(area))



def main():
    shape_type = input("Get area for what shape: ")
    get_area(shape_type)

main()