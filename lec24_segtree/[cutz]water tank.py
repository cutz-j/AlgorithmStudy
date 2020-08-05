import sys

def dfs(i, liter):
    visited[i] = True
    
    
    adj_list = adj.get(i+1, [])
    for j in adj_list:
        if visited[j-1] == False:
            dfs(j-1, liter+1)
    dfs_order.append(i+1)
    score.append(liter)
    

def dfs_all():
    for i in range(N):
        if visited[i] == False:
            dfs(i, 1)


def init():
    t = 1
    while t <= N:
        t *= 2
        
    for i in range(N):
        tree[t+i] = score[i]
    
    for i in range(t-1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1]

def update(x, diff):
    t = 1
    while t <= N:
        t *= 2
    
    tx = t + x
    while tx < 1:
        tree[tx] += diff
        tx /= 2

rl = input
# rl = lambda: sys.stdin.readline()

N, C = map(int, rl().split())

adj = {}
for _ in range(N-1):
    x, y = map(int, rl().split())
    if len(adj.get(x, [])) != 0:
        adj[x].append(y)
    else:
        adj[x] = [y]

visited = [False for _ in range(N)]
Q = int(rl())
dfs_order, score = [], []
dfs_all()
dfs_order = dfs_order[::-1]
tree = [0] * (N*4)
init()
for _ in range(Q):
    query, city = map(int, rl().split())
    
    if query == 1:
#        update(dfs_order.index(city), score.index(city))
        pass
        
        
        
    elif query == 2:
        pass
