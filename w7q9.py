def merge_and_sort(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list


list1 = [12, 45, 23, 67]
list2 = [89, 34, 56, 1]

sorted_list = merge_and_sort(list1, list2)

print("Merged and Sorted List:", sorted_list)
