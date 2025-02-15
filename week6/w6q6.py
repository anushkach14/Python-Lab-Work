b=float(input("Enter base of triangle: "))
h=float(input("Enter height of triangle: "))

area=1/2*b*h
print(f"Area of traingle is: {area}")

a=int(input("Enter side 1: "))
b=int(input("Enter side 2: "))
c=int(input("Enter side 3: "))

if a==b==c:
    print("Equilateral triangle")

if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
    print("Isosceles triangle")

if (a != b != c) and a!=c:
    print("Scalene triangle")

