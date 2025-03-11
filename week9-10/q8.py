# Sample dictionary
my_dict = {
    'apple': 50,
    'banana': 30,
    'cherry': 40,
    'date': 60,
    'elderberry': 20
}

# Sorting the dictionary by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sorting the dictionary by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Displaying the results
print("Dictionary sorted by value in ascending order:")
print(sorted_dict_asc)

print("\nDictionary sorted by value in descending order:")
print(sorted_dict_desc)
