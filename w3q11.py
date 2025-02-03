n = int(input("Enter a number: "))
a, b = 0, 1
while a < n:
    a, b = b, a + b
if a == n:
    print(f"{n} is a Fibonacci number.")
else:
    print(f"{n} is not a Fibonacci number.")
