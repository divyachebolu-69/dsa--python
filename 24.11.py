nums = [3, 1, 2]
for i in range(len(nums) - 1):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            print("Swap", nums[j], "and", nums[j + 1])
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)  