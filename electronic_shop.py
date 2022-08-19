def getMoneySpent(k, d, b):
    m = 0
    if min(k) >= b or min(d) >= b or min(k) + min(d) >= b:
        return -1

    for i in k:
        for j in d:
            if i+j > m and i+j <= b:
                m = i+j
    return m

if __name__ == "__main__":
    bnm = input().split()
    b = int(bnm[0])
    keyboard = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboard, drives, b)
    print(moneySpent)
