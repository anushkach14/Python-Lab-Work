import math

def largest(a,b,c):
    return max(a,b,c)


def volume(shape, *dimensions):
    if shape == "cylinder":
        r, h = dimensions
        return math.pi * r**2 * h
    elif shape == "cube":
        side = dimensions[0]
        return side**3
    elif shape == "rectangular box":
        l, b, h = dimensions
        return l * b * h
    else:
        return "Invalid shape"

def area_of_rect(l, b):
    return l * b


def circumference(r):
    return 2 * math.pi * r


def exchange_values(a, b):
    return b, a


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Main function to interact with the user
def main():

    print("Enter three numbers to find the largest:")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    print("The largest number is:", largest(num1, num2, num3))


    shape = input("\nEnter the shape (cylinder, cube, rectangular box): ").lower()
    if shape == "cylinder":
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        print("The volume of the cylinder is:", volume(shape, radius, height))
    elif shape == "cube":
        side = float(input("Enter the side of cube: "))
        print("The volume of cube is:", volume(shape, side))
    elif shape == "rectangular box":
        length = float(input("Enter length of rectangular box: "))
        width = float(input("Enter width of rectangular box: "))
        height = float(input("Enter height of rectangular box: "))
        print("The volume of the rectangular box is:", volume(shape, length, width, height))
    else:
        print("Invalid shape.")


    l = float(input("\nEnter length of rectangle: "))
    b = float(input("Enter width of rectangle: "))
    print("The area of rectangle is:", area_of_rect(l, b))


    radius = float(input("\nEnter radius of circle: "))
    print("The circumference of circle is:", circumference(radius))


    a = float(input("\nEnter the first value: "))
    b = float(input("Enter the second value: "))
    a, b = exchange_values(a, b)
    print(f"After exchange, first value is: {a} and second value is: {b}")


    x1, y1 = float(input("\nEnter x1: ")), float(input("Enter y1: "))
    x2, y2 = float(input("Enter x2: ")), float(input("Enter y2: "))
    print("The distance between the two points is:", distance(x1, y1, x2, y2))

if __name__ == "__main__":
    main()
