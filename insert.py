def insert_at_position(arr, value, pos):
    arr.insert(pos, value)
    return arr

arr = [10, 20, 30, 40]
print("Before:", arr)
insert_at_position(arr, 25, 2)
print("After inserting 25 at position 2:", arr)