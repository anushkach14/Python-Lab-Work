# Function to implement bubble sort
def bubble_sort(arr):
    # Traverse through all elements in the list
    for i in range(len(arr)):
        # Compare adjacent elements
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Input: Taking a list of numbers from the user
user_input = input("Enter numbers separated by spaces: ")
arr = [int(x) for x in user_input.split()]

# Sorting the list using bubble sort
bubble_sort(arr)

# Displaying the sorted list
print("Sorted list:", arr)
