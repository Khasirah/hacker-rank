def breakingRecords(scores):
    # min = 0
    # max = 0
    # cMin = 0
    # cMax = 0

    # for score in scores:
    #     if min == 0 and max == 0 and scores.index(score) == 0:
    #         min = score
    #         max = score
    #         print(max, min)
    #         continue

    #     if score > max:
    #         max = score
    #         cMax = cMax + 1
    #         print(max, min, cMax, cMin)

    #     if score < min:
    #         min = score
    #         cMin = cMin + 1
    #         print(max, min, cMax, cMin)

    # return [cMax, cMin]

    # Solution Internet
    lo = scores[0]
    hi = scores[0]
    lob = 0
    hib = 0
    for i in range(1,len(scores)):
        if scores[i] < lo:
            lob += 1
            lo = scores[i]
        if scores[i] > hi:
            hib += 1
            hi = scores[i]
    return [hib, lob]
            

if __name__ == "__main__":
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
