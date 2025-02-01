import math

def sum_of_num():
    numbers=input("Enter as many no. as you want to get added: ").split()
    tot=0
    for i in numbers:
        tot += int (i)
    return tot

print("Sum of numbers is: ",sum_of_num())
