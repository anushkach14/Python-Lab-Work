string = input("Enter string: ")
c = dict()
txt = string.split(" ")
for t in txt:
	if t in c:
		c[t] += 1
	else:
		c[t] = 1
print(c)