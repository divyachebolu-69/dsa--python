def delete_at_position(arr, pos):
    if 0 <= pos < len(arr):
        arr.pop(pos)
    else:
        print("Position out of range")
    return arr

arr = [10, 20, 25, 30, 40]
print("Before:", arr)
delete_at_position(arr, 2)
print("After deleting position 2:", arr)