import sys
import math
import heapq

inf = sys.maxsize

def dijkstra(graph, k):
    prev = [-1] * (len(graph)+1)
    dist = [inf]*(len(graph)+1)
    dist[k] = 0
    
    priority_queue = []
    heapq.heappush(priority_queue, [0, k])
    
    while priority_queue:
        current_dist, here = heapq.heappop(priority_queue)

        # 인접 노드 iteration
        for there, length in graph[here].items():
            next_dist = dist[here] + length

            if next_dist < dist[there]:
                dist[there] = next_dist
                prev[there] = here
                heapq.heappush(priority_queue, [next_dist, there])
    return dist, prev

rl = lambda : sys.stdin.readline()
# rl = input
for _ in range(int(rl())):
    n, m = map(int, rl().split())
    graph = [[0]*n]*n
        
    for i_ in range(m):
        a, b, c = map(int, rl().split())
            
        if b in graph[a]:
            graph[a][b] = math.log(min(graph[a][b], c))
        else:
            graph[a][b]= math.log(c)
    
    dist, prev = dijkstra(graph, n)
    for d in dist[1:]:
        print(d if d != inf else "INF")