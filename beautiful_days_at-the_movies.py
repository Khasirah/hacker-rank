def reverseNum(num):
    stringToReverse = list(str(num))
    stringToReverse.reverse()
    return int("".join(stringToReverse))

def beautifulDays(i,j,k):
    # beautiful days
    bd = 0
    for i in range(i,j+1):
        if abs(i - reverseNum(i))%k == 0:
            bd += 1
    return bd


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    i = int(first_multiple_input[0])
    j = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    result = beautifulDays(i,j,k)
    print(result)
