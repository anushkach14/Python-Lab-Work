def circle_area(r):
    return 3.14159 * r**2

radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.3f}")
