
def consecutive(a):
    a.sort()
    return all(a[i] - a[i - 1] == 1 for i in range(1, len(a)))


a = [1,2,3,45,5,6]
print(consecutive(a))