def birtdayCakeCandle(arr):
    arrMax = max(arr)
    countMax = 0

    for i in arr:
        if i == arrMax:
            countMax = countMax + 1

    return countMax


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(birtdayCakeCandle(arr))
    print("percobaan dengan apa ini namanya")
