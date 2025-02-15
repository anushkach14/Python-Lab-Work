n = int(input("Enter a number: "))

if n < 2:
    print(f"{n} is not a prime number.")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number. First factor: {i}")
            break
    else:
        print(f"{n} is a prime number.")
