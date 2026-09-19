def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


s = list(input("Enter a string: "))
reverse_string(s)
print("Reversed string:", "".join(s))