import sys

def tiling(n):
    if n <= 1:
        return 1
    
    if cache.get(n, -1) != -1:
        return cache[n]
    
    cache[n] = (tiling(n-1) + tiling(n-2)) % 10007
    return cache[n]


#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())
cache = {}

print(tiling(N))