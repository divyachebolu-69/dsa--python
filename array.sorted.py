def check_sorted(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return "Ascending"
    elif all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return "Descending"
    else:
        return "Not sorted"

a1 = [1, 2, 3, 4, 5]
a2 = [5, 4, 3, 2, 1]
a3 = [3, 1, 4, 1, 5]
print(a1, "->", check_sorted(a1))
print(a2, "->", check_sorted(a2))
print(a3, "->", check_sorted(a3))