mylist=[list(map(int,x.split())) for x in input("Enter elements of list: ").split()]
print(mylist)
for i in range(len(mylist)):
    print(f"Element at index {i}: ",mylist[i])