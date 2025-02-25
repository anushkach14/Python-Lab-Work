def gdcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

print(gdcd(50,10))
