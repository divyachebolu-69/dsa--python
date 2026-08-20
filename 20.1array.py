def sortArr(arr):
    arr.sort()
    return arr[-1]

if __name__ == "__main__":
    arr1 = [2, 5, 7, 9, 0]
    arr2 = [8, 6, 10, 11, 12]

    print("the Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))
