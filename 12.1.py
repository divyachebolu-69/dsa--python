nums = [10, 45, 32, 45, 8, 27]

largest = second = float("-inf")
for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest:", second)