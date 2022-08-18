def countingValley(s, p):
    l = 0
    pos = 0
    temp_pos = 0
    
    for i in range(s):
        if p[i] == "U":
            pos += 1
        
        if p[i] == "D":
            pos -= 1

        if pos == 0 and temp_pos == -1:
            l += 1

        temp_pos = pos

    return l

if __name__ == "__main__":
    s = int(input().strip())
    p = input()
    result = countingValley(s, p)
    print(result)
