import sys
sys.setrecursionlimit(30000)

def genius(time, song):
    # Recursive DP 불가능 --> k=1,000,000 일때 maximum recursive 
    if time > k:
        if song == p:
            return 1
        else:
            return 0
    
    if cache.get((time, song), -1) != -1:
        return cache[(time, song)]
    
    ret = 0
    for i in range(n):
        ret += genius(time + length[i], i) * T[song][i]
    cache[(time, song)] = ret 
    return ret
        
    
    
#rl = lambda : sys.stdin.readline()
rl = input
C = int(rl())
for _ in range(C):
    n, k, m = map(int, rl().split())
    length = list(map(int, rl().split()))
    T = []
    for i in range(n):
        t_row = list(map(float, rl().split()))
        T.append(t_row)
    prefer = list(map(int, rl().split()))
    time = 0
    
    res = ''
    for p in prefer:
        cache = {}
        res += str(genius(time+length[0], 0))
        if prefer.index(p) != len(prefer)-1:
            res += ' '
    print(res)