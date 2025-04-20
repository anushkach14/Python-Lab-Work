data = {"b": 20, "a": 35,"c":50}
value = int(input("Enter value to search: "))

for key, val in data.items():
    if val == value:
        print(f"Key for value {value}: {key}")
        break
else:
    print("Value not found")
