def selection_sort_desc(nums):
    n = len(nums)
    for pos in range(n - 1):
        max_index = pos
        for j in range(pos + 1, n):
            if nums[j] > nums[max_index]:     
                max_index = j
        nums[pos], nums[max_index] = nums[max_index], nums[pos]
    return nums

print(selection_sort_desc([29, 10, 14, 37, 13]))   