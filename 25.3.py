def modify_string(s):
    new_str = s
    new_str += "World"
    return new_str
original = "Hello"
result = modify_string(original)

print("original:", original)
print("Returned:" , result)