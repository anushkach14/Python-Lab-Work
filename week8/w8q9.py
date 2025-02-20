def rev_str(str):
    x=str.split()
    return " ".join(x[::-1])

str1=input("Enter a string : ")
print(rev_str(str1))