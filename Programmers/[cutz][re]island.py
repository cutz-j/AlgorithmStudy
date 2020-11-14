import heapq
from collections import defaultdict
import sys

sys.setrecursionlimit(999999)

answer = 0


def dfs(i, adj, cond, visited):
    global answer
    print(visited)
    visited[i] = True
    for j, c in adj[i]:
        print("adj", j, c)
        if not visited[j]:
            if cond[j] == c:
                print(i, j, c)
                answer += c
                dfs(j, adj, cond, visited)


def solution(n: int, costs: list) -> int:
    #     global answer
    #     # n: length of islands
    #     # costs: cost
    #     # i, j, cost
    #     # all visited
    #     # 모든 노드에서 들어오는 최소 edge
    #     cond = defaultdict(lambda: sys.maxsize)
    #     adj = defaultdict(list)
    #     stack, visited = [], [False]*n
    #     for i, j, cost in costs:
    #         if cost < cond[i]:
    #             cond[i] = cost
    #         if cost < cond[j]:
    #             cond[j] = cost
    #         adj[i].append((j, cost))
    #         adj[j].append((i, cost))

    #     for i in range(n):
    #         for j, c in adj[i]:
    #             if j == 0 and cond[j] == c:
    #                 dfs(i, adj, cond, visited)

    #     for i in range(n):
    #         if not visited[i]:
    #             dfs(i, adj, cond, visited)

    # kruskal algorithm
    ans = 0
    costs.sort(key=lambda x: x[2])  # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]])  # 집합
    while len(routes) != n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans