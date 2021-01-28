from collections import defaultdict, deque
import math
import sys

sys.setrecursionlimit(99999999)

row_dir, col_dir = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(i: int, j: int, visited: list, group: int, land: list, height: int) -> None:
    visited[i][j] = group
    for k in range(4):
        new_i, new_j = i + row_dir[k], j + col_dir[k]
        if 0 <= new_i < len(land) and 0 <= new_j < len(land):
            if visited[new_i][new_j] == 0:
                diff = abs(land[new_i][new_j] - land[i][j])
                if diff <= height:
                    dfs(new_i, new_j, visited, group, land, height)
    return


def fine_h(visited: list, height: int, land: list, table: dict) -> None:
    for i in range(len(land)):
        for j in range(len(land)):
            ri, dj = i + 1, j + 1
            if dj < len(land) and visited[i][j] != visited[i][dj]:
                a, b = min(visited[i][j], visited[i][dj]), max(visited[i][j], visited[i][dj])
                table[(a, b)] = min(table[(a, b)], abs(land[i][j] - land[i][dj]))
            if ri < len(land) and visited[i][j] != visited[ri][j]:
                a, b = min(visited[i][j], visited[ri][j]), max(visited[i][j], visited[ri][j])
                table[(a, b)] = min(table[(a, b)], abs(land[i][j] - land[ri][j]))


def find_p(x: int, par: list) -> int:
    # union-find
    if x == par[x]:
        return x
    else:
        p = find_p(par[x], par)
        par[x] = p
        return p


def union_find(x: int, y: int, parent: list) -> None:
    x = find_p(x, parent)
    y = find_p(y, parent)
    parent[y] = x


def solution(land: list, height: int) -> int:
    answer = 0
    queue = deque()
    visited = [[0 for _ in range(len(land))] for __ in range(len(land))]
    group = 1
    # dfs
    for i in range(len(land)):
        for j in range(len(land)):
            if not visited[i][j]:
                dfs(i, j, visited, group, land, height)
                group += 1

    # for v in visited:
    #     print(v)
    ###### MST #######
    table = defaultdict(lambda: math.inf)
    fine_h(visited, height, land, table)
    table = sorted(table.items(), key=lambda x: x[1])
    nodes = {i: i for i in range(1, group)}  # unique group num
    for (a, b), value in table:
        if find_p(a, nodes) != find_p(b, nodes):
            union_find(a, b, nodes)
            answer += value
        if len(nodes.values()) == 1:
            return answer
    return answer