def avg(num1, num2, num3, num4, num5):
    return (num1 + num2 + num3 + num4 + num5) / 5

def fahrenheit(celsius):
    return (celsius * 9/5) + 32

def perimeter(l, b):
    return 2 * (l + b)

print("Enter five numbers to compute the average:")
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))
average = avg(num1, num2, num3, num4, num5)
print("Average of the five numbers:", average)

cel = float(input("\nEnter temperature in Celsius: "))
f = fahrenheit(cel)
print(f"{cel}°C is equal to {f}°F")

l= float(input("\nEnter the length of the rectangle: "))
b = float(input("Enter the width of the rectangle: "))
peri = perimeter(l, b)
print("Perimeter of the rectangle:", peri)
