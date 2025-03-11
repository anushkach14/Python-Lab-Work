# Taking input from the user as a space-separated string of numbers
user_input = input("Enter elements separated by spaces: ")

# Converting the input string into a list of integers
mylist = [int(x) for x in user_input.split()]

# Sorting the list in ascending order
mylist.sort()

# Displaying the sorted list
print(f"The sorted list is: {mylist}")
