def sortArrayByParity(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums

print(sortArrayByParity([3, 1, 2, 4]))   