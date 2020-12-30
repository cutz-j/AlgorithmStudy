import sys
import heapq

def find(start):
    dist = [sys.maxsize] * (N+1)
    ans = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        w, e = heapq.heappop(heap)
        adj_vec = adj[e]
        for a_w, a_e in adj_vec:
            new_w = w + a_w
            if new_w < dist[a_e]:
                dist[a_e] = new_w
                heapq.heappush(heap, (new_w, a_e))
    
    ans += dist[X]
    dist = [sys.maxsize] * (N+1)
    heap = []
    heapq.heappush(heap, (0, X))
    while heap:
        w, e = heapq.heappop(heap)
        adj_vec = adj[e]
        for a_w, a_e in adj_vec:
            new_w = w + a_w
            if new_w < dist[a_e]:
                dist[a_e] = new_w
                heapq.heappush(heap, (new_w, a_e))
    
    ans += dist[start]
    return ans


rl = input
# rl = lambda: sys.stdin.readline()


adj = {}
N, M, X = map(int, rl().split())
for _ in range(M):
    s, e, w = map(int, rl().split())
    
    tmp = adj.get(s, [])
    if tmp:
        tmp.append((w, e))
    else:
        adj[s] = [(w, e)]

best_ans = 0       
for n in range(1, N+1):
    if n == X:
        continue
    ans = find(n)
    if ans > best_ans:
        best_ans = ans

print(best_ans)
    