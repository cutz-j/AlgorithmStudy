import sys

MAX = 30
best = sys.maxsize
dist = []
min_edge = [MAX]

def simpleHeuristic(visited):
    ret = min_edge[0]
    for i in range(n):
        if visited[i] == False:
            ret += min_edge[i]
        return ret

def search(path, visited, current_length):
    global best
    
#    if best <= current_length: # pruning
    if best <= current_length + simpleHeuristic(visited): # simple heuristic
        return
    
    here = path[-1]
    
    if len(path) == n:
        best = min(best, current_length+dist[here][0])
        return
    
    for nt in range(n):
        if visited[nt] == True:
            continue
        
        path.append(nt)
        visited[nt] = True
        search(path, visited, current_length+dist[here][nt])
        visited[nt] = False
        path.pop()
        
rl = input

n = int(rl())
for _ in range(n):
    dist.append(list(map(float, rl().split())))

visited = [False for _ in range(n)]
path = [0]
visited[0] = True

search(path, visited, 0)

print(best)