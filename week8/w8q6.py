str=input("Enter a string of characters: ")
freq={}
for char in lst:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1

print(freq)