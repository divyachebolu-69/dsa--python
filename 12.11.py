nums = [12, 7, 9, 20, 33, 4]

even = [n for n in nums if n % 2 == 0]
odd = [n for n in nums if n % 2 != 0]

print("Even:", even, "Count:", len(even))
print("Odd:", odd, "Count:", len(odd))