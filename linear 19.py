def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i         
    return -1                

print(linear_search([4, 9, 1, 7], 1))   
print(linear_search([4, 9, 1, 7], 5))    