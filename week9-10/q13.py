# Function to implement Quick Sort
def quick_sort(arr):
    # Base case: if the list has 1 or no element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose the last element as the pivot
    pivot = arr[-1]
    
    # Partition the list into two halves: one with elements less than pivot, the other with elements greater than pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively sort the left and right halves, and then combine them with the pivot in the middle
    return quick_sort(left) + [pivot] + quick_sort(right)

# Input: Taking numbers from the user
user_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in user_input.split()]

# Sorting the list using Quick Sort
sorted_arr = quick_sort(arr)

# Displaying the sorted list
print("Sorted list:", sorted_arr)
