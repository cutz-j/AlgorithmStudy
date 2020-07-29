import sys

def product(present_idx, idx_arr, dp_arr):
    if len(dp_arr) == N:
        return cache[tuple(dp_arr)]
    
    if cache.get(tuple(dp_arr), -1) != -1:
        return cache[tuple(dp_arr)]
    
    dp_arr.append(idx_arr.pop(present_idx))
    r, c = mat[present_idx]
    for i in idx_arr:
        a, b = mat[i]
        if c == a:
            cache[tuple(dp_arr)] = cache.get(tuple(dp_arr), 0) + (r*c*b), 
    
    return cache[tuple(dp_arr)] 
        
        



rl = input
# rl = lambda: sys.stdin.readline()

N = int(rl())

mat = []
cache = {}
idx = [i for i in range(N)]
dp = []
for _ in range(N):
    r, c = map(int, rl().split())
    mat.append((r, c))
    
