import heapq
from collections import defaultdict
import sys

sys.setrecursionlimit(999999)

answer = sys.maxsize


def dfs(i, adj, cond, visited):
    global answer
    print(visited)
    visited[i] = True
    for j, c in adj[i]:
        print("adj", j, c)
        # if not visited[j]:
        if cond[j] == c:
            print(i, j, c)
            answer += c
            dfs(j, adj, cond, visited)


def solution(n: int, costs: list) -> int:
    global answer
    # n: length of islands
    # costs: cost
    # i, j, cost
    # all visited
    # 모든 노드에서 들어오는 최소 edge
    cond = defaultdict(lambda: sys.maxsize)
    adj = defaultdict(list)
    stack, visited = [], [False] * n
    for i, j, cost in costs:
        if cost < cond[i]:
            cond[i] = cost
        if cost < cond[j]:
            cond[j] = cost
        adj[i].append((j, cost))
        adj[j].append((i, cost))

    for i in range(n):
        for j, c in adj[i]:
            if j == 0 and cond[j] == c:
                answer = c
                visited[i] = True

    for i in range(n):
        if not visited[i]:
            dfs(i, adj, cond, visited)

    return answer