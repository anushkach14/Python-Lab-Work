a=float(input("Enter num 1:"))
b=float(input("Enter num 2:"))
c=float(input("Enter num 3:"))
if a>=b and a>=c:
    print(f"The greatest number is : {a}")
elif b>=a and b>=c:
    print(f"The greatest number is : {b}")
else:
    print(f"The greatest number is : {c}")
    