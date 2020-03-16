import sys

def genius(time, song):
    log = (time, song)
    if time > k:
        return cache[log]
    if cache.get(log, -1) != -1:
        return cache[log]
    
    cache[log] = 0.0
    for i in range(1, n):
        cache[log] += genius(time - length[i], i-1) * T[i-1][i]
        
    return cache[log]
        
    
    

#rl = lambda : sys.stdin.readline()
rl = input
C = int(rl())
for _ in range(C):
    cache = {}
    n, k, m = map(int, rl().split())
    length = list(map(int, rl().split()))
    T = []
    for i in range(n):
        t_row = list(map(float, rl().split()))
        T.append(t_row)
    prefer = list(map(int, rl().split()))
    time = 0
    
    genius(time, 0)