import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def search(A):
    graph = defaultdict(list)
    bool_map = [[False for _ in range(N)] for __ in range(N)]

    for i in range(N):
        for j in range(N):
            if i < N-1:
                if L <= abs(A[i][j] - A[i+1][j]) <= R:
                    graph[(i,j)].append((i+1, j))
                    graph[(i+1,j)].append((i, j))
            # else:
            #     if L <= abs(A[i][j] - A[i][j+1]) <= R:
            #         graph[(i,j)].append((i,j+1))
            #         graph[(i,j+1)].append((i,j))
            if j < N-1:
                if L <= abs(A[i][j] - A[i][j+1]) <= R:
                    graph[(i,j)].append((i, j+1))
                    graph[(i, j+1)].append((i, j))
    return graph, bool_map

def dfs(g, visited):
    for new_g in graph[g]:
        if visited[new_g[0]][new_g[1]] == False:
            visited[new_g[0]][new_g[1]] = True
            linked.append(A[new_g[0]][new_g[1]])
            g_list.append(new_g)
            dfs(new_g, visited)

rl = lambda: sys.stdin.readline()

N, L, R = map(int, rl().split())

A = []
for _ in range(N):
    A.append(list(map(int, rl().split())))

time = 0
while True:
    graph, visited = search(A)
    # print(graph)
    # for a in A:
    #     print(a)
    if not graph:
        break
    linked, g_list = [], []
    for g in graph:
        dfs(g, visited)
        # if linked:
        #     for v in visited:
        #         print(v)
        # print(linked)
        if linked:
            population = int(sum(linked) / len(linked))
            for fg in g_list:
                A[fg[0]][fg[1]] = population
            linked, g_list = [], []
    time += 1

print(time)
