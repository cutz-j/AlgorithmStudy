import sys

def product(present_idx, idx_arr, dp_arr):
    if len(dp_arr) == N-1:
        return sys.maxsize
    
    if cache.get(tuple(dp_arr), -1) != -1:
        return cache[tuple(dp_arr)]
    
    dp_arr.append(present_idx)
    idx_arr.remove(present_idx)
    r, c = mat[present_idx]
    for i in idx_arr:
        a, b = mat[i]
        if c == a:
            result = min(cache.get(tuple(dp_arr), 0)+r*c*b, product(i, idx_arr, dp_arr))
            cache[tuple(dp_arr)] = result
    
    return result
        

# 먼저 쌍을 만들고 가야할지.
# dp list --> 빨리 참



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
    
