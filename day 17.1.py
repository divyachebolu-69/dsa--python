import time

nums_list = list(range(1_000_000))
nums_set = set(nums_list)
target = 999_999

start = time.time()
print(target in nums_list)
print("List lookup:", time.time() - start)

start = time.time()
print(target in nums_set)
print("Set lookup: ", time.time() - start)