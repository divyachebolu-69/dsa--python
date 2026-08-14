original = [1, 2, 3, 4, 5]
copy_arr = original.copy()  
print("Original:", original)
print("Copy:", copy_arr)

copy_arr[0] = 999
print("After modifying copy -> Original:", original, " Copy:", copy_arr)