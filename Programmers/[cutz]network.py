from collections import defaultdict
import sys

sys.setrecursionlimit(99999999)


def dfs(idx, adj, visited):
    visited[idx] = True

    for a in adj[idx]:
        if not visited[a]:
            dfs(a, adj, visited)


def solution(n: int, computers: list) -> int:
    # n: # of computers
    # computers: adj matrix
    answer = 0
    adj = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                print(i, j)
                adj[i].append(j)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, adj, visited)
            answer += 1
    return answer