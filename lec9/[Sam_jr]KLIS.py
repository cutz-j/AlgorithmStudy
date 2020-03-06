# -*- coding: utf-8 -*-



def lis(start):
    ret = cacheLen[start+1]
    if ret!= -1:
        return ret
    ret = 1
    next_ = start+1
    for s in range(next_):
        if start == 0 or (s[start] < S[next_]):
            ret = max(ret,lis(next_)+1)
    return ret

def count(start):
    if lis(start) == 1:
        return 1
    ret = cacheCnt[start+1]
    if ret != -1:
        return ret
    
    ret = 0
    for i in range(start+1,n):
        if (start == -1) or (S[start] < S[i]) and (lis(start) == lis(i)+1):
            ret = min(MAX,ret+count(i))
    
    cacheCnt[start+1] = ret
    return ret

if __name__ == '__main':
    MAX = 200000001
    test_case = int(input())
    for t in range(test_case):
        num_el,k = [int(x) for x in input().split()]
        num_seq = [int(x) for x in input().split()]
        n = 0
        cacheLen = [[-1]*501]
        cacheCnt = [[-1]*501]
        S = [[-1]*500]
        print(count(0))


