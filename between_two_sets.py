def getTotalX(a,b):
    x = 0

    # for bNum in b:
        # if all(bNum % aNum == 0 for aNum in a):
            # x = x + 1

    for i in range(1,101):
        if all(i%x == 0 for x in a) and all(x%i == 0 for x in b):
            x = x + 1

    return x

if __name__ == '__main__':
    first_input = input().rstrip().split()

    n = int(first_input[0])
    m = int(first_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
