num = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to search: "))

print(f"Found at index {num.index(x)}" if x in num else "Not found")
