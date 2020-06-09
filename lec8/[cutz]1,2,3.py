import sys


def recursive(N, num):
    global freq
    if num == N:
        freq += 1
        return 
    elif num > N:
        return
    
    recursive(N, num+1)
    recursive(N, num+2)
    recursive(N, num+3)
    return freq
        
def dp(N):
    cache = [0 for i in range(N+1)]
    cache[1] = 1
    cache[2] = 2
    cache[3] = 4
    
    for i in range(4, N+1):
        cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
        
    return cache


#rl = lambda: sys.stdin.readline()
rl = input


T = int(rl())
cache = dp(10)
for _ in range(T):
    N = int(rl())
#    freq = 0
    print(cache[N])
    
    