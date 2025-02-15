def fibo(n):
    n1, n2 = 0, 1
    for _ in range(n):
        print(n1, end=" ")
        n1, n2 = n2, n1 + n2

num = int(input("How many Fibonacci numbers would you like to generate? "))
fibo(num)
