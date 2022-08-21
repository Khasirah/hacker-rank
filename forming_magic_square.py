import itertools


def isMagic(s):
    for i in range(3):
        if sum(s[i*3:i*3+3]) != 15:
            return False
        if sum(s[i::3]) != 15:
            return False

    if s[0] + s[4] + s[8] != 15:
        return False

    if s[2] + s[4] + s[6] != 15:
        return False

    return True

def formingMagicSquare(s):
    costMin = 1000
    for p in itertools.permutations(range(1,10)):
        cost = sum([abs(p[i]-s[i]) for i in range(len(s))]) 
        if cost < costMin and isMagic(p):
            costMin = cost
    return costMin

if __name__ == "__main__":
    s = []
    for _ in range(3):
        s.extend(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
