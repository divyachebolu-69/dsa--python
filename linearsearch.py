def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print("Array:", arr)
print("Index of 30:", linear_search(arr, 30))
print("Index of 99:", linear_search(arr, 99))
