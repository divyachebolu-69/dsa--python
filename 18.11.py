
def total(nums):
    s = 0
    for n in nums:
        s += n
    return s


def doubled(nums):
    return [n * 2 for n in nums]