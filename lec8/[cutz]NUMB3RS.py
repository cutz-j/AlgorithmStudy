import sys


def bruteforce(path):
    # time over
    if len(path) == D+1: # 0일에 1개를 넣기 때문.
        if path[-1] != q:
            return 0.0
#        print("path", path)
        result = 1.0
        for i in range(0, len(path)-1):
            result /= deg[path[i]] # path 전까지의 확률 계산
        return result
    
    result = 0.0
    for i in range(N):
        if A[path[-1]][i] == 1:
            path.append(i)
            result += bruteforce(path) # path까지의 후보들 모두 summation
            path.pop(-1)
    return result

def dp(here, days):
    if days == D:
        if here == q:
            return 1.0
        else:
            return 0.0
    
    if cache.get((here, days), -1) != -1:
        return cache[(here, days)]
    
    ret = 0.0
    for i in range(N):
        if A[here][i] == 1:
            ret += dp(i, days+1) / deg[here]
    cache[(here, days)] = ret
    return ret

def dp_reverse(here, days):
    # q부터 reverse 계산
    # 그 전날 어디에 숨어있을 지를 계산
    if days == 0:
        if here == P:
            return 1
        else:
            return 0
   
    if cache.get((here, days), -1) != -1:
        return cache[(here, days)]
    
    ret = 0
    for i in range(N):
        if A[here][i] == 1:
            ret += dp_reverse(i, days-1) / deg[i]
    cache[(here, days)] = ret
    return ret
    

            
#rl = lambda : sys.stdin.readline()
rl = input

C = int(rl())
for _ in range(C):
    A = []
    N, D, P = map(int, rl().split())
    for __ in range(N):
        A.append(list(map(int, rl().split())))
    T = int(rl())
    Q = list(map(int, rl().split()))
    deg = []
    for i in range(N):
        tmp = 0
        for j in range(N):
            if A[i][j] == 1:
                tmp += 1
        deg.append(tmp)
    
#    path = [P]
    res = ''
    for q in Q:
        cache = {}
        res += str(dp_reverse(q, D))
        if Q.index(q) != len(Q)-1:
            res += ' '
            
#    for q in Q: # q가 바뀔때 연산 수가 증가
#        cache = {}
##        res += str(bruteforce(path))
#        res += str(dp(P, 0))
#        if Q.index(q) != len(Q)-1:
#            res += ' '
    
    print(res)