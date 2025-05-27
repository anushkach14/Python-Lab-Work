def sum(n):
    total = 0
    while n > 0:
        total += n % 10  
        n = n // 10  
    return total

num = int(input("Enter a decimal integer: "))

print(f"The sum of the digits of {num} is: {sum(num)}")
''' or
n=[int(x) for x in input("Enter an integer: ")]
print(sum(n))
