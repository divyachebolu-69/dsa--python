def count_even_odd(arr):
    even = sum(1 for x in arr if x % 2 == 0)
    odd = len(arr) - even
    return even, odd

arr = [1, 2, 3, 4, 5, 6, 7]
print("Array:", arr)
even, odd = count_even_odd(arr)
print("Even count:", even)
print("Odd count:", odd)