a=float(input("Enter num 1:"))
b=float(input("Enter num 2:"))
c=float(input("Enter num 3:"))
if a<=b and a<=c:
    print(f"The smallest number is : {a}")
elif b<=a and b<=c:
    print(f"The smallest number is : {b}")
else:
    print(f"The smallest number is : {c}")
    