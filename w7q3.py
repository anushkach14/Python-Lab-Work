def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
    
limit=int(input("Enter number of terms: "))

if limit<=0:
    print("Enter a positive number!!")
else:
    print("Fibonacci series: ")
    for i in range(limit):
        print(fibo(i),end=' ')
