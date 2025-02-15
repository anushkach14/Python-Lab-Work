def is_perfect(num):
    if num <= 0:
        return False 
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

x = int(input("Enter a number: "))

if is_perfect(x):
    print(f"{x} is a perfect number.")
else:
    print(f"{x} is not a perfect number.")
