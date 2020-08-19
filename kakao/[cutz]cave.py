result = []

def dfs(here, visited, adj, dependency, bool_graph):
    visited[here] += 1
    if bool_graph.get(here, True) == False:
        return
    if dependency.get(here, None):
        bool_graph[dependency[here]] = True
    
    for there in adj[here]:
        dfs(there, visited, adj, dependency, bool_graph)
    result.append(here)

def solution(n, path, order):
    answer = True
    adj = {}
    for a, b in path:
        if adj.get(a, []):
            adj[a].append(b)
        else:
            adj[a] = [b]
        if adj.get(b, []):
            adj[b].append(a)
        else:
            adj[b] = [a]
    dependency = {a:b for a, b in order}
    bool_graph = {b:False for a, b in order}
    
    visited = [0] * n
    for i in range(n):
        dfs(i, visited, adj, dependency, bool_graph)
    
            
    return answer