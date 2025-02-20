def sq_tuple(n):
    result=[(i,i**2) for i in range(1,n+1)]
    return result

n=int(input("Enter number of elements to get sqaured: "))
print("List: ",sq_tuple(n))