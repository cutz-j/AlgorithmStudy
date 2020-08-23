result = []

def dfs(here, visited, adj):
    visited[here] += 1    
    for there in adj.get(here, []):
        if visited[there] == 0:
            dfs(there, visited, adj)
    result.append(here)

def solution(n, path, order):
    global result
    
    answer = True
    adj = {}
    for a, b in path:
        if adj.get(a, []):
            adj[a].append(b)
        else:
            adj[a] = [b]
    for a, b in order:
        if adj.get(a, []):
            adj[a].append(b)
        else:
            adj[a] = [b]
            
    
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, adj)
    
    result = result[::-1]
    for i in range(n):
        for j in range(i+1, n):
            if adj.get(result[j], []):
                if result[i] in adj[result[j]]:
                    return False

    return answer

# binary search