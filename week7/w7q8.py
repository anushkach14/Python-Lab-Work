def separate(nums):
    even_nums = []
    odd_nums = []

    for n in nums:
        if n % 2 == 0:
            even_nums.append(n)
        else:
            odd_nums.append(n)

    return even_nums, odd_nums


nums =[int(x) for x in input("Enter list elements: ").split()]
even_nums, odd_nums = separate(nums)

print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
