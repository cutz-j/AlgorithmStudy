import sys

def pill(w, h):
    # DP
    if cache.get((w, h), 0) != 0:
        return cache[(w, h)]
    # basis
    if w == 0: # W가 0일 경우 (모두 반조각 남았을 때), 무조건 1
        return 1
    
    cache[(w, h)] = pill(w-1, h+1)
    if h > 0:
        cache[(w, h)] += pill(w, h-1)
        
    return cache[(w, h)]
    


#rl = lambda: sys.stdin.readline()
rl = input


while True:
    N = int(rl())
    if N == 0:
        break
    cache = {}
    
    print(pill(N, 0))
    
    
    
    
