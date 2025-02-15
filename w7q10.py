def second_largest(nums):

    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


    return nums[-2]

numbers = [12, 45, 88, 23, 45, 89, 67]
print("The second largest number is:", second_largest(numbers))
