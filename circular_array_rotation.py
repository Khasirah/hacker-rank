def circularArrayRotation(a, k, q):
    ans = []
    for _ in range(k):
        a.insert(0, a[-1])
        a.pop(-1)
    for i in range(len(q)):
        ans.append(a[q[i]])
    
    return ans

if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    q = int(first_multiple_input[2])
    a = list(map(int, input().rstrip().split()))
    queries = []

    for _ in range(q):
        queries_item = int(input().rstrip())
        queries.append(queries_item)
    
    result = circularArrayRotation(a, k, queries)
    print('\n'.join(map(str, result)))