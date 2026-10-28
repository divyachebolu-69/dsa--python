def printTillN(n):
    if n == 0:
        return
    printTillN(n - 1)
    print(n, end=' ')


if __name__ == "__main__":
    n = 3
    printTillN(n)