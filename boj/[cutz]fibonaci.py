from collections import defaultdict
import sys
import time
sys.setrecursionlimit(9999999)

def exhaust(n):
    if n <= 1:
        return n

    return exhaust(n-2) + exhaust(n-1)

def memoization(n):
    if cache[n]:
        return cache[n]

    if n <= 1:
        return n

    cache[n] = memoization(n-2) + memoization(n-1)
    return cache[n]

def tabulation(n):
    cache = defaultdict(int)
    cache[0] = 0
    cache[1] = 1
    for i in range(2, n+1):
        cache[i] = cache[i-2] + cache[i-1]
    return cache[i]


start = time.time()
print(exhaust(30))
print("time: ", time.time() - start)

cache = defaultdict(int)
start = time.time()
print(memoization(1000))
print("time: ", time.time() - start)

start = time.time()
print(tabulation(1000))
print("time: ", time.time() - start)


