def migrationBirds(arr):
    s = []
    c = 0
    m = 0
    
    for i in range(len(arr)):
        if len(s) > 0:
            for j in range(len(s)):

                if arr[i] == s[j][0]:
                    break

                if arr[i] != s[j][0]:
                    if j == len(s)-1:
                        s.append([arr[i], arr.count(arr[i])])


        if len(s) == 0:
            s.append([arr[i], arr.count(arr[i])])

    for ss in s:
        if ss[1] > m:
            m = ss[1]
    
    print(s)

    for i in range(len(s)):
        if s[i][1] == m and c == 0:
            c = s[i][0]
        if s[i][1] == m:
            if s[i][0] > c:
                continue

    return c

    # count = [0] * 6
    # for i in arr:
    #     count[i] += 1
    # print(count)
    # print(count.index(max(count)))
    # return 0

if __name__ == "__main__":
    arr_count = int(input().strip())
    arr = list(map(int,input().rstrip().split()))
    result = migrationBirds(arr)
    print(result)
