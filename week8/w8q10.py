def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = list(map(int, input("Enter sorted elements to find element using Binary Search -").split()))
target = int(input("The element to search for: "))
print(binary_search(arr, target))
