def selection_sort(nums):
    n = len(nums)
    for pos in range(n - 1):
        min_index = pos
        for j in range(pos + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[pos], nums[min_index] = nums[min_index], nums[pos]
    return nums