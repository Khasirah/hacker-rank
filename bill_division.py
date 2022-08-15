def bonAppetit(bill, k, b):
    s = 0
    for i in range(len(bill)):
        if i == k:
            continue

        s = s + bill[i]

    s = s / 2

    if s == b:
        print("Bon Appetit")
        return

    print(int(b - s))
    return

if __name__ == "__main__":
    first = input().rstrip().split()
    n = int(first[0])
    k = int(first[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
