import sys

# recursive --> dp
def make(X):
    for i in range(1, X+1):
        cache[i] = cache.get(i-1, -1) + 1
        if i % 3 == 0:
            cache[i] = min(cache.get(i, -1), cache.get(int(i/3), -1)+1)
        if i % 2 == 0:
            cache[i] = min(cache.get(i, -1), cache.get(int(i/2), -1)+1)
        
    return cache[X]
#    return min(min(a,b),c)


#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())
cache = {}
print(make(N))