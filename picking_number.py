def pickingNumber(a):
    # angka patokan
    ap = 0
    # tempat hasil sementara
    hs = 0
    # hasil terbaik
    ht = 0
    a.sort()
    for a_itr in a:
        if ap == 0 or abs(ap - a_itr) > 1:
            ap = a_itr
            hs = 0
        if abs(ap - a_itr) <= 1:
            hs += 1
        if ht < hs:
            ht = hs
    return ht



if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().rstrip().split()))
    result = pickingNumber(a)
    print(result)
