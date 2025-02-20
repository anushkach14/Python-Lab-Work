list1=input("Enter elements of list 1: ").split(",")
list2=input("Enter elements of list 2: ").split(",")

union_list=list(set(list1) | set(list2))
print("Union of list: ", union_list)