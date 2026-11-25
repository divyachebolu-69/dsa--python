nums = sorted([41, 21, 41, 11, 21, 51])         
unique = [nums[0]]

for n in nums[1:]:
    if n != unique[-1]:
        unique.append(n)

print(unique)  