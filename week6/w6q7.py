r1=int(input("Enter the starting range (r1<r2): "))
r2=int(input("Enter the ending of range: "))

if (r1<r2):
    num=list(range(r1,r2+1))
    print(num)
else:
    print("Oops. You entered r2>r1")

