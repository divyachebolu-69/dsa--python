def rotate_left(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k] if k != 0 else arr[:]

arr = [1, 2, 3, 4, 5, 6, 7]
print("Original:", arr)
print("Rotate left by 2:", rotate_left(arr, 2))
print("Rotate right by 2:", rotate_right(arr, 2))