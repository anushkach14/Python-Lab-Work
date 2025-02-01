s = input("Enter string: ")
vowels = "aeiouAEIOU"
counts = {}

for char in s:
    if char in vowels:
        counts[char] = counts.get(char, 0) + 1  # Update the count

print(counts)
