def diagonalDifference(arr):

    d1 = 0
    d2 = 0
    arrLength = len(arr)
    
    for row in range(arrLength):
        for col in range(arrLength):
            if row == col:
                d1 = d1 + arr[row][col]
            
        d2 = d2 + arr[row][arrLength - 1 - row] 
    
    if (d1 - d2) > 0:
        return d1 - d2

    return (d1 - d2) * (-1)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    results = diagonalDifference(arr)
    print(results)
