def printSolidRectangle(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print("* ", end="")
            print()

if __name__ == "__main__":
    n, m = 3, 5
    printSolidRectangle(n, m)