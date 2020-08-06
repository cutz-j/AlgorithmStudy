# -*- coding: utf-8 -*-
from heapq import heappush, heappop

test_case = int(input())
for _ in range(test_case):
    num_vert, num_edges,burn,num_fireD = [int(x) for x in input().split()]
    adj = [[] for _ in range(num_vert)]

    input_l = []
    for _ in range(num_edges):
        input_l.append([int(x) for x in input().split()])

    for x in input_l:
        adj[x[0]].append((x[-1],x[1]))
        adj[x[1]].append((x[-1],x[0]))
    
    burn_loc = [int(x) for x in input().split()]
    fd_loc = [int(x) for x in input().split()]

    #best = firetrucks(start=fd_loc)
    

    h = [(0, a) for a in fd_loc]
    best = [float('inf') for i in range(num_vert)]
    
    for a in fd_loc:
        best[a] = 0
        print('best=',best)
    
    while h:
        cost, here = heappop(h)
        if best[here] < cost:
            continue
    
        for addCost, there in adj[here]:
            nextCost = cost + addCost
            if best[there] > nextCost:
                best[there] = nextCost
                heappush(h, (nextCost, there))
ans  =sum((best[a] for a in burn_loc))
print(ans)
