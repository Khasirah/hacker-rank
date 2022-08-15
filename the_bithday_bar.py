def birthday(s,d,m):
    wdc = 0
    ans = []
 
    for j in range(len(s)):
        if (len(s) - j) < m:
            return wdc

        while len(ans) < m:
            for i in range(j, j+m):
                ans.append(s[i])

        if sum(ans) == d:
            wdc = wdc + 1

        ans.clear()

    return wdc

if __name__ == "__main__":
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)
