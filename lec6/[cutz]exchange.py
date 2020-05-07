import sys


def change_number(n, i, j):
    if i == j:
        return n
    return int(str(n)[:i] + str(n)[j] + str(n)[i+1:j] + str(n)[i] + str(n)[j+1:])

def exchange(n, i, j, k):
    if len(str(n)) != length:
        return -1
    if k == K+1:
        return n
    if cache.get((n, i, j), -1) != -1:
        return cache[(n, i, j)]
    
    new_num = change_number(n, i, j)
    for idx in range(length-1):
        for jdx in range(idx+1, length):
            cache[(n, i, j)] = max(cache.get((n, i, j), -1), exchange(new_num, idx, jdx, k+1))
    return cache[(n, i, j)]


#rl = lambda: sys.stdin.readline()
rl = input

N, K = map(int, rl().split())
cache = {}
length = len(str(N))
k_list = []
ret = exchange(N, 0, 0, 0)
print(ret)