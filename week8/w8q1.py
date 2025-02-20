def sort_list(list1):
    return sorted(list1,key=len)

lst=[x.split(",") for x in input("enter list elements(sprt sublists using ';'' ): ").split(";")]

print("Sorted List: ",sort_list(lst))
