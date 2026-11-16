def containsNearbyDuplicate(nums, k):
    last = {}
    for i, n in enumerate(nums):
        if n in last and i - last[n] <= k:
            return True
        last[n] = i
    return False

print(containsNearbyDuplicate([1, 2, 3, 1], 3))        
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  