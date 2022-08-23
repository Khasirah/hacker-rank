def climbingTheLeaderboard(r, p):
    # hasil
    h = []
    # ranking saat ini
    rSI = 0
    for p_itr in p:
        for i in range(len(r)):
            if i == 0 or r[i] != r[i-1]:
                rSI += 1
            
            if p_itr > r[i] and rSI == 1:
                h.append(rSI)
                break

            if p_itr > r[i]:
                h.append(rSI)
                break

            if p_itr == r[i]:
                h.append(rSI)
                break

            if (p_itr < r[i]) and (i == len(r)-1):
                h.append(rSI+1)
                continue

            if p_itr < r[i]:
                continue            
        rSI = 0

    return h

def answerInternet(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)
    
    l=len(ranked)
    j=0
    
    ans=[]
    for i in range(len(player)):
        while j<l and player[i]<ranked[j]:
            j+=1
        
        ans.append(j+1)
        
    return ans[::-1] 

if __name__ == "__main__":
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingTheLeaderboard(ranked, player)
    print('\n'.join(map(str, result)))
    print('\n')
