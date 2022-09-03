def viralAdvertising(n):
    # kumulatif like
    kl = 0
    # recipient
    r = 0
    for i in range(n):
        if i == 0:
            r = (int(5/2)*3)
            kl += int(5/2)
            continue
        kl += int(r/2)
        r = (int(r/2)*3)
    return kl

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)