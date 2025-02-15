def sec_largest(nums):
    nums.sort()
    return nums[-2] if len(nums) >= 2 else None

nums = [12, 45, 69, 20, 45, 89, 67]
result = sec_largest(nums)
print(f"The second largest number is: {result}")
