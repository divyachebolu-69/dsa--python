def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)
        return

    arr.sort()

    small = arr[1]
    large = arr[n -2]
    print ("second smallest is " ,small)
    print ("second largest  is ", large)
    if __name__ == "__main__ " :
        arr = [1, 2, 4, 6 , 7, 5]
        n = len(arr)
        getElements(arr, n)