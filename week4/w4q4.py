def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

num = int(input("Enter an integer: "))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"The factorial of {num} is: {factorial(num)}")
