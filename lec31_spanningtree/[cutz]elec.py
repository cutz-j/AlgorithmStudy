import sys

def find(x):
    k = []
    while parent[x] != x:
        k.append(x)
        x = parent[x]
    
    for i in k:
        parent[i] = x
    
    return x

def merge(a, b):
    parent[a] = b


rl = input
# rl = lambda: sys.stdin.readline()
while True:
    m, n = map(int, rl().split())
    if m == n == 0:
        break
    adj = []
    ans = 0
    for _ in range(n):
        x, y, z = map(int, rl().split())
        adj.append((z, (x, y)))
        ans += z
    
        
    adj.sort()
    
    parent = {i:i for i in range(m)}
    
    cnt, sum_cost = 0, 0
    for i in range(n):
        cost = adj[i][0]
        x = adj[i][1][0]
        y = adj[i][1][1]
        
        x, y = find(x), find(y)
        if x == y:
            continue
        
        cnt += 1
        sum_cost += cost
        merge(x, y)
    
    ans -= sum_cost
    print(ans)

