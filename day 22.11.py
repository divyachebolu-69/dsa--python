
def key(x):
    return (x % 2, x)

nums = [5, 2, 8, 1, 4]
n = len(nums)
for pos in range(n - 1):
    min_index = pos
    for j in range(pos + 1, n):
        if key(nums[j]) < key(nums[min_index]):
            min_index = j
    nums[pos], nums[min_index] = nums[min_index], nums[pos]

print(nums)                                        