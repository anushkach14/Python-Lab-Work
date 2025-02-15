def del_odd(str):
    result=''

    for i in range(len(str)):
        if i%2==0:
            result += str[i]
        
    return result

str=input("Enter a string : ")
print("Output: ",del_odd(str))
