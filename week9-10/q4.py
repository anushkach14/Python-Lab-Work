num = list(map(int, input("Enter a list of numbers to find the avg: ").split()))
average = sum(num) / len(num) if num else 0
print(average)
