def find_min_index(nums, start):
    min_index = start                      
    for i in range(start + 1, len(nums)):
        if nums[i] < nums[min_index]:     
            min_index = i
    return min_index