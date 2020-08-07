import sys
import heapq

rl = input
# rl = lambda:sys.stdin.readline()


N = int(rl())
parts = []
for _ in range(N):
    parts.append(list(rl()))
    
present, transform = map(int, rl().split())

adj = [[] for _ in range(N)]
for i in range(len(parts)):
    for j in range(i+1, len(parts)):
        part_a, part_b = parts[i], parts[j]
        w = 0
        for k in range(len(part_a)):
            w += (int(part_a[k]) - int(part_b[k]))**2
        adj[j].append((w, i))
        adj[i].append((w, j))
            

heap = []
dist = [sys.maxsize]*(N)
heapq.heappush(heap, (0, present-1))
while heapq:
    w, v = heapq.heappop(heap)
    adj_vec = adj[v]
    for d, a in adj_vec:
        new_w = w + d
        if new_w < dist[a]:
            dist[a] = new_w
            heapq.heappush(heap, (new_w, a))

print(dist[transform-1])