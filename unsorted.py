def remove_duplicates_unsorted(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

arr = [4, 2, 7, 2, 4, 9, 7, 1]
print("Original:", arr)
print("After removing duplicates (order preserved):", remove_duplicates_unsorted(arr))