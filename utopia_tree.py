def utopiaTree(n):
    # tinggi awal
    ta = 1
    for n_itr in range(n+1):
        if n_itr == 0:
            continue
        if n_itr % 2 == 1:
            ta *= 2
        if n_itr % 2 == 0:
            ta += 1
    
    return ta

if __name__ == "__main__":
    t = int(input().strip())
    
    for t_itr in range(t):
        n = int(input().strip())
        result = utopiaTree(n)
        print(result)
