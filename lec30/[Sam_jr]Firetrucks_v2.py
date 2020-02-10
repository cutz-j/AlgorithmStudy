from heapq import heappush, heappop




def Dij(start):
    global adj
    
    h = [(0, a) for a in start]
    
    for i in h:
        adj[0].append(i)
    
    best = [float('inf') for i in range(num_vert)]
    
    for a in fd_loc:
        best[a-1] = 0      

    while h:
        cost, here = heappop(h)
        if best[here-1] < cost:
            continue
    
        for addCost, there in adj[here]:
            
            nextCost = cost + addCost
            if best[there-1] > nextCost:
                best[there-1] = nextCost
                heappush(h, (nextCost, there))

    return best

if __name__ == '__main__':
    test_case = int(input())
    for _ in range(test_case):
        num_vert, num_edges,burn,num_fireD = [int(x) for x in input().split()]
        adj = [[] for _ in range(num_vert+1)]
    
        input_l = []
        for _ in range(num_edges):
            input_l.append([int(x) for x in input().split()])
    
        for x in input_l:
            adj[x[0]].append((x[-1],x[1]))
            adj[x[1]].append((x[-1],x[0]))
        
        burn_loc = [int(x) for x in input().split()]
        fd_loc = [int(x) for x in input().split()]
        best = Dij(fd_loc)
        ans = sum((best[a-1] for a in burn_loc))
        print(ans)