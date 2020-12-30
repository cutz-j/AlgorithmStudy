import sys
import math

pi = math.pi
inf = sys.maxsize

def solveLinear(begin, end):
    used, idx = 0, 0
    while(begin < end):
        max_cover = -1
        while(idx < n and info_sort[idx][0] <= begin):
            max_cover = max(max_cover, info_sort[idx][1])
            idx += 1
        if max_cover <= begin:
            return inf
        begin = max_cover
        used += 1
    return used

def solverCirbular():
    ret = inf
    
    for i in range(n):
        if info_sort[i][0] <= 0 or info_sort[i][1] >= 2*pi:
            begin = math.fmod(info_sort[i][1], 2*pi)
            end = math.fmod(info_sort[i][0]+2*pi, 2*pi)
            ret = min(ret, 1 + solveLinear(begin, end))
    return ret

rl = lambda: sys.stdin.readline()
#rl = input

C = int(rl())

for _ in range(C):
    n = int(rl())
    info = []
    for __ in range(n):
        i = tuple(map(float, rl().split()))
                
        loc = math.fmod(2*pi + math.atan2(i[0], i[1]), 2*pi)
        rg = 2.0 * math.asin(i[2] / 2.0 / 8.0)
        
        info.append((loc-rg, loc+rg))

    info_sort = sorted(info)

    answer = solverCirbular()
    
    if answer != inf:
        print(answer)
    else:
        print("IMPOSSIBLE")
        
    
        
        
        


    