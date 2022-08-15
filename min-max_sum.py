def miniMaxSum(arr):
    arrMin = min(arr)
    arrMax = max(arr)
    sumMin = sum(arr) - arrMax
    sumMax = sum(arr) - arrMin

    print(f"{sumMin} {sumMax}")


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

