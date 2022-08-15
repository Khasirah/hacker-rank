def divisibleSumPairs(n, k, ar):
    pairs = 0

    for i in range(len(ar)):
        if i == (len(ar) - 1):
            return pairs
        for j in range(i + 1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                pairs += 1

    return pairs

if __name__ == "__main__":
    f_multi_input = input().rstrip().split()
    n = int(f_multi_input[0])
    k = int(f_multi_input[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    print(result)
