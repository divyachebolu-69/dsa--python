def count_halvings(n):
    steps = 0
    while n > 1:
        n //= 2            
        steps += 1
    return steps

print(count_halvings(1_000_000))   