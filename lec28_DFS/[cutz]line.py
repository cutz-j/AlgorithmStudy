import sys

def dfs(a):
    global order
    visited[a] = True
    
    for i in adj.get(a, []):
        if visited[i] == False:
            dfs(i)
    order.append(a+1)

def dfsAll():
    for i in range(N):
        if visited[i] == False:
            dfs(i)
    
    

rl = input
# rl = lambda: sys.stdin.readline()
order = []
N, M = map(int, rl().split())
visited = [False]*N
adj = {}
for _ in range(M):
    A, B = map(int, rl().split())
    tmp = adj.get(A-1, [])
    tmp.append(B-1)
    adj[A-1] = tmp

dfsAll()
for i in range(len(order)):
    print(order[-(i+1)], end=' ')