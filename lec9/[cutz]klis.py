import sys
import math

MAX = 200000000 + 1
cache_len = [-1]*501
cache_cnt = [-1]*501
S = [-1]*500

n = 0

def lis(start):
    ret = cache_len[start+1]
    if ret != -1:
        return ret
    
    ret = 1
    for n_ in range(start+1, n):
        if (start == 1) or (S[start] < S[n_]):
            ret = max(ret, lis(n_)+1)
    cache_len[start+1] = ret
    return ret

def count(start):
    if lis(start) == 1:
        return 1
    
    ret = cache_cnt[start+1]
    if ret != -1:
        return ret
    ret = 0
    for n_ in range(start+1, n):
        if (start == -1) or (S[start] < S[n_]) and (lis(start) == lis(n_)+1):
            ret = min(MAX, ret+count(n_))
    cache_cnt[start+1] = ret
    return ret
            

rl = input
#rl = lambda : sys.stdin.readline()

C = int(rl()) # m = word lenfth, q = sentences length
for _ in range(C):
    n, k = map(int, rl().split())
    num = map(int, rl().split())
    
    print(count(0))
