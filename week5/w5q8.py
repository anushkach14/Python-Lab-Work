str=input("ENTER A STRING: ")   
words=str.split()
rev=""

for i in reversed(words):     #i=word
    rev += i+" "

rev=rev.strip()
print(rev)