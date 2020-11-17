import heapq
from collections import defaultdict
import sys


def solution(n: int, costs: list) -> int:
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