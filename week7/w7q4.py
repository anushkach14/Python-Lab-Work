def fact(n):
    if n==1:
        return n
    else:
        return n* fact(n-1)
    
num=int(input("Enter a  number: "))

if num ==0:
    print("Factorial of 0 = 1")
else:
    print(f"Factorial of {num} is ",fact(num))
