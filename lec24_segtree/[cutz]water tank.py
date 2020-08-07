import sys

def dfs(i, liter, cnt):
    visited[i] = True
    cnt_all = cnt
    adj_list = adj[i+1]
    for j in adj_list:
        if visited[j-1] == False:
            cnt += 1
            dfs(j-1, liter+1, cnt)
    if cnt_all != cnt:
        child = cnt - cnt_all
        cnt_list[i] = childp
    dfs_order.append(i+1)
    score.append(liter)

def init():
    t = 1
    while t <= N:
        t *= 2
        
    for i in range(N):
        tree[t+i] = 0
    
    for i in range(t-1, 0, -1):
        tree[i] = tree[2*i] + tree[2*i+1]

def update(x):
    t = 1
    while t <= N:
        t *= 2
    
    tx = t + x
    while tx >= 1:
        tree[tx] += 1
        tx //= 2

def query_sum(l, r):
    t = 1
    while t <= N:
        t *= 2
    tl = t+l
    tr = t+r
    s = 0
    while tl <= tr:
        if tl % 2 == 1:
            s += tree[tl]
            tl += 1
        elif tr % 2 == 0:
            s += tree[tr]
            tr -= 1
        tl //= 2
        tr //= 2
    return s


rl = input
# rl = lambda: sys.stdin.readline()

N, C = map(int, rl().split())
cnt = 0
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, rl().split())
    adj[x].append(y)
    
cnt_list = [0] * N*4
visited = [False for _ in range(N*4)]
Q = int(rl())
dfs_order, score = [], []
dfs(0, 1, 0)
dfs_order = dfs_order[::-1]
score = score[::-1]
tree = [0] * (N*4)
dfs_idx_dict = {value:idx for idx, value in enumerate(dfs_order)}

#init()
for _ in range(Q):
    query, city = map(int, rl().split())
    
    if query == 1:
        idx = dfs_idx_dict[city]
        s = score[idx]
        update(idx)
            
    elif query == 2:
        idx = dfs_idx_dict[city]
        s = score[idx]
        child = cnt_list[idx]
        left, right = idx, idx+child
        print(query_sum(left, right) * s)
            
        
