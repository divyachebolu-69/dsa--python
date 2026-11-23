def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        print("Pass", i + 1, "→", nums)
        if not swapped:
            break
    return nums

bubble_sort([5, 1, 4, 2, 8])