import sys

def dfs(a):
    global order
    visited[a] = True
    for i in cities.get(a, []):
        if visited[i] == False:
            order.append(i)
            dfs(i)
    return order
            

def dfs_all():
    global order
    cnt = 0
    for i in range(n):
        if visited[i] == False:
            cnt += 1
            road_cnt = dfs(i)
    return cnt, len(road_cnt)

def find(n, lib_cost, road_cost, cities):
    
    res = n * lib_cost
    cnt, road_cnt = dfs_all()
    new_res = (cnt*lib_cost) + (road_cnt*road_cost)
    if res < new_res:
        return res
    else:
        return new_res


rl = input
# rl = lambda: sys.stdin.readline().

q = int(rl())
for _ in range(q):
    n, m, lib_cost, road_cost = map(int, rl().split())
    cities = {}
    for __ in range(m):
        start, end = map(int, rl().split())
        
        if cities.get(start-1, -1) != -1:
            cities[start-1].append(end-1)
        else:
            cities[start-1] = [end-1]
            
        if cities.get(end-1, -1) != -1:
            cities[end-1].append(start-1)
        else:
            cities[end-1] = [start-1]
        
    order = []
    visited = [False for i in range(n)]
    res = find(n, lib_cost, road_cost, cities)
    print(res)