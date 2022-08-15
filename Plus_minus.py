def plusMinus(arr):
    countPositive = 0
    countNegative = 0
    countZero = 0
    arrLen = len(arr)

    for i in arr:
        if i > 0:
            countPositive = countPositive + 1

        if i < 0:
            countNegative = countNegative + 1

        if i == 0:
            countZero = countZero + 1

    print(round(countPositive / arrLen,4))
    print(round(countNegative / arrLen,4))
    print(round(countZero / arrLen,4))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
