num=int(input("Enter a number: "))
orig=num
sum=0
n=len(str(num))
while num>0:
    digit=num%10
    sum += digit**n
    num //= 10

if sum==orig:
    print(f"{orig} is an Armstrong number.")
else:
    print(f"{orig} is not an Armstrong number.")