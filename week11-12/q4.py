def reverse_lookup(dictionary, value):
    for key,val in dictionary.items():
        if val==value:
            return key
    return None

data={
    "apple":1,
    "mango":2,
    "computer":3,
    "AMU":4,
    "anushka":5
}

val_search=int(input("Enter the value to search for: "))
key=reverse_lookup(data,val_search)

if key:
    print(f"Key for value {val_search} is '{key}'.")
else:
    print(f"Value {val_search} not found!")