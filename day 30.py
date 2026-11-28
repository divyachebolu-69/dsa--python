n = int(input())
low, high, ans = 0, n, 0
while low <= high:
    mid = (low + high) // 2
    if mid * mid <= n:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)