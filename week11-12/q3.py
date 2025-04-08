letter_str=input("Enter a string: ")
letter_count={}
for char in letter_str:
    if char.isalpha():
        char=char.lower()
        letter_count[char]=letter_count.get(char, 0) + 1

for letter,count in letter_count.items():
    print(f"{letter}: {count}")