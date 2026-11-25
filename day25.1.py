nums = sorted([9, 6, 7, 3, 2, 5])        
unique = [nums[0]]

for n in nums[1:]:
    if n != unique[-1]:
        unique.append(n)

print(unique)  