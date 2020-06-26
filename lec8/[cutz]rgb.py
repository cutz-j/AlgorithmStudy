import sys
sys.setrecursionlimit(10**6)

def pick(c, cur, prev_idx):
    # exhastive search
    print(c, cur, prev_idx)
    global answer
    
    if cur == N:
        return c
    
    for i in range(3):
        if i == prev_idx:
            continue
        
        tmp_c = pick(c+cost[cur][i], cur+1, i)
        if tmp_c < answer:
            answer = tmp_c
            
    return answer

def pick_dp(cur, prev_idx):
    if cur == N:
        return 0
    
    if cache.get((cur, prev_idx), -1) != -1:
        return cache[(cur, prev_idx)]

    ret = sys.maxsize
    for i in range(3):
        if i == prev_idx:
            continue
        ret = min(ret, pick_dp(cur+1, i)+cost[cur][i])
    
    cache[(cur, prev_idx)] = ret
    return cache[(cur, prev_idx)]




#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())
cost = []
for _ in range(N):
    cost.append(list(map(int, rl().split())))

#answer = sys.maxsize
#print(pick(0, 0, None))
cache = {}
print(pick_dp(0, None))