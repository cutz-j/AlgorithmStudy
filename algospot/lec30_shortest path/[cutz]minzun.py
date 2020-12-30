#from queue import PriorityQueue
import heapq
import sys


rl = input
# rl = lambda: sys.stdin.readline()
V, E, P = map(int, rl().split())

adj = [[] for i in range(10000)]
for _ in range(E):
    a, b, c = map(int, rl().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

heap = []
dist = [sys.maxsize] * 10000
heapq.heappush(heap, (0, 1))
dist[1] = 0
while len(heap) != 0:
    w, v = heapq.heappop(heap)
    adj_ver = adj[v]
    for d, a in adj_ver:
        new_dist = w + d
        if new_dist < dist[a]:
            dist[a] = new_dist
            heapq.heappush(heap, (new_dist, a))

heap = []
dist_pv = [sys.maxsize] * 10000
heapq.heappush(heap, (0, P))
dist_pv[P] = 0
while len(heap) != 0:
    w, v = heapq.heappop(heap)
    adj_ver = adj[v]
    for d, a in adj_ver:
        new_dist = w + d
        if new_dist < dist_pv[a]:
            dist_pv[a] = new_dist
            heapq.heappush(heap, (new_dist, a))
  
  
first_dist = dist[V]
second_dist = dist[P] + dist_pv[V]

if first_dist == second_dist:
    print("SAVE HIM")
else:
    print("GOOD BYE")