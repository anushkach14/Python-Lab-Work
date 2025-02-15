def separate(nums):
    even_nums = []
    odd_nums = []

    for n in nums:
        if n % 2 == 0:
            even_nums.append(n)
        else:
            odd_nums.append(n)

    return even_nums, odd_nums


nums = [12, 45, 67, 23, 44, 89, 56, 78]
even_nums, odd_nums = separate(nums)

print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
