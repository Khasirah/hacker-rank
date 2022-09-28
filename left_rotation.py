def rotateLeft(d, arr):
    ans = []
    for i in range(len(arr[d:])):
        ans.append(arr[d+i])
    
    for i in range(len(arr[:d])):
        ans.append(arr[i])

    return ans

if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    print(result)