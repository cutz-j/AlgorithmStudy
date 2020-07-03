import sys


rl = lambda : sys.stdin.readline()
#rl = input

C = int(rl())

for _ in range(C):
    N = int(rl())
    pair = {}
    
    M = list(map(int, rl().split()))
    E = list(map(int, rl().split()))
    
    for i, e in enumerate(E):
        pair[i] = e
        
    pair_sort = sorted(pair.items(), key = lambda item: item[1], reverse=True) # value: [1]
    ret, eat = 0, 0
    for i in range(N):
        box = pair_sort[i][0]
        eat += M[box]
        ret = max(ret, eat + E[box])
        
    print(ret)