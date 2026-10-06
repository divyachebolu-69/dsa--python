arr = [10, -5, 7, -2, 8, -9]

positive = 0
negative = 0

for num in arr:
    if num > 0:
        positive += 1
    else:
        negative += 1

print("Positive:", positive)
print("Negative:", negative)