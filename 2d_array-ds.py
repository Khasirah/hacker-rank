def hourglassSum(arr):
    ans = []
    for r in range(1,len(arr)):
        for c in range(1,len(arr[r])):
            try:
                jml = arr[r-1][c-1] + arr[r-1][c] + arr[r-1][c+1] + arr[r][c] + arr[r+1][c-1] + arr[r+1][c] + arr[r+1][c+1]
                ans.append(jml)
            except: 
                continue

    
    return max(ans)

if __name__ == "__main__":
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = hourglassSum(arr)
    print(result)