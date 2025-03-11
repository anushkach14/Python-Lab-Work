"""import array
num=array.array('i',[int(x) for x in input("Enter elements: ").split()])
num.reverse()
print("Reversed array: ",num)"""
import array

# Taking input from the user for 5 integers
numbers = array.array('i', [int(x) for x in input("Enter 5 integers separated by spaces: ").split()])

# Reversing the order of the items in the array
numbers.reverse()

# Displaying the reversed array
print("\nThe reversed array:", numbers)
