mylist=[int(x) for x in input("enter elements: ").split()]
find=int(input("Enter element to search: " ))
for i in range(len(mylist)):
    if mylist[i]==find:
        print(f"Element {find} is present at index{i}")
    else:
        print("Element is not present in the list!")

