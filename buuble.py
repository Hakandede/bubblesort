def sortcheck():
    global isSorted
    sortCount = 0
    for i in range(len(arr)):
        if i + 1 < len(arr):
            if arr[i] <= arr[i + 1]:
                sortCount += 1
    if sortCount + 1 == len(arr):
        isSorted = True
        print("-----Dataset is sorted!--------")
    else:
        isSorted = False
        print("is sorted false")
        sort()


def sort():
    global arr, rangevalue

    for i in range(rangevalue - 1):

        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(arr)
    sortcheck()


arr = [987, 7987, 54, 321, 2, 546, 87, 54, 2132, 588, 4569, 45, 44, 1, 0]
rangevalue = len(arr)
sort()
