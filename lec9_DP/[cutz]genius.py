import sys
import math
import copy

sys.setrecursionlimit(30000)

def genius(time, song):
    # Recursive DP 불가능 --> k=1,000,000 일때 maximum recursive 
    if time > k:
        if song == p:
            return 1
        else:
            return 0
    
    if cache.get((time, song), -1) != -1:
        return cache[(time, song)]
    
    ret = 0
    for i in range(n):
        ret += genius(time + length[i], i) * T[song][i]
    cache[(time, song)] = ret 
    return ret
        
def genius_it():
    W = [[0.0 for _ in range(4*n)] for __ in range(4*n)]
    for i in range(3*n):
        W[i][i+n] = 1.0
        
    for i in range(n):
        for j in range(n):
            W[3*n+i][(4-length[j])*n+j] = T[j][i]
    
    Wk = copy.deepcopy(W)
    
    def mat_pow(Wk):
        res = []
        for k in range(4*n):
            d_list = []
            for i in range(4*n):
                dummy = 0
                for j in range(4*n):
                    dummy += Wk[k][j]*W[j][i]
                d_list.append(dummy)
            res.append(d_list)
        return res
    
    for i in range(n-1):
        res = mat_pow(Wk)
        Wk = copy.deepcopy(res)
    
    ret = [0.0 for _ in range(n)]
    for song in range(n):
        for start in range(length[song]):
            ret[song] += Wk[(3-start)*n + song][3*n]
    return ret
            
    
#rl = lambda : sys.stdin.readline()
rl = input
C = int(rl())
for _ in range(C):
    n, k, m = map(int, rl().split())
    length = list(map(int, rl().split()))
    T = []
    for i in range(n):
        t_row = list(map(float, rl().split()))
        T.append(t_row)
    prefer = list(map(int, rl().split()))
    time = 0
    
    res = ''
#    for p in prefer:
#        cache = {}
#        res += str(genius(time+length[0], 0))
#        res += str(genius_it)
#        if prefer.index(p) != len(prefer)-1:
#            res += ' '
    print(genius_it())