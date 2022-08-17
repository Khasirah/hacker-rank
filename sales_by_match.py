def sockMerchant(n, ar):
    p = []

    for i in range(n):
        if i == (n-1):
            break
        if i in p:
            continue
        
        for j in range(i+1,n):
            if(ar[i] == ar[j]):
                p.append(i)
                p.append(j)
                break

    return int(len(p)/2)

if __name__ == "__main__":
   n = int(input().strip())
   ar = list(map(int, input().rstrip().split()))
   result = sockMerchant(n, ar)
   print(result)
