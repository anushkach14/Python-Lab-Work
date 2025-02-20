def str_ends(str):
    if len(str)<2:
        return ""
    return str[:2] + str[-2:]

str1=input("Enter a string of characters: ")
print(str_ends(str1))