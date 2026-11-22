def median(nums):
    n = len(nums)
    for pos in range(n // 2 + 1):
        min_index = pos
        for j in range(pos + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[pos], nums[min_index] = nums[min_index], nums[pos]
    return nums[n // 2]

print(median([7, 1, 5, 3, 9]))        