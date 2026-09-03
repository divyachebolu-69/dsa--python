def pattern10(N):
    for i in range(1, 2 * N):
        
        stars = i
        
        if i > N:
            stars = 2 * N - i
        
        for j in range(stars):
            print("*", end="")
        
        print()

N = 5
pattern10(N)