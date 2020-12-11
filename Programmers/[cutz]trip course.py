import sys
from collections import defaultdict
import heapq

sys.setrecursionlimit(9999999)
answer = []


def dfs(arrival, adj):
    while adj[arrival]:
        arr = heapq.heappop(adj[arrival])
        dfs(arr, adj)
    answer.append(arrival)


def solution(tickets):
    global answer
    # build graph (heap)
    # dfs -> topological sort
    adj = defaultdict(list)
    for s, e in tickets:
        adj[s].append(e)

    for a in adj:
        heapq.heapify(adj[a])

    dfs('ICN', adj)
    answer = answer[::-1]
    return answer