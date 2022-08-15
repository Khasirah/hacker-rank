def countApplesAndOranges(s, t, a, b, m, n, apples, oranges):
    countApples = 0
    countOranges = 0

    # menghitung apel yang jatuh di rumah sam
    for i in apples:
        if (a + i >= s) and (a + i <= t):
            countApples += 1

    # menghitung jeruk yang jatuh di rumah sam
    for i in oranges:
        if (b + i >= s) and (b + i <= t):
            countOranges += 1

    print(countApples)
    print(countOranges)


if __name__ == "__main__":
    first_input = input().rstrip().split()

    s = int(first_input[0])
    t = int(first_input[1])

    second_input = input().rstrip().split()

    a = int(second_input[0])
    b = int(second_input[1])

    third_input = input().rstrip().split()

    m = int(third_input[0])
    n = int(third_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, m, n, apples, oranges)
