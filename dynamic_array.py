def dynamicArray(n,q):
    ans = []
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    for a in q:
        print(a)
        idx = ((a[1] ^ lastAnswer) % n)
        if a[0] == 1:
            arr[idx].append(a[2])

        if a[0] == 2:
            lastAnswer = arr[idx][a[2] % len(arr[idx])]
            ans.append(lastAnswer)
    return ans

if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    
    result = dynamicArray(n, queries)

    print(result)