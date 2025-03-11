# Merge Sort Function
def merge_sort(arr):
    # Base case: list with one or no element is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)

# Helper function to merge two sorted lists
def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # Compare each element of both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Add any remaining elements from both lists
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Input: Taking numbers from the user
user_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in user_input.split()]

# Sorting the list using merge sort
sorted_arr = merge_sort(arr)

# Displaying the sorted list
print("Sorted list:", sorted_arr)
