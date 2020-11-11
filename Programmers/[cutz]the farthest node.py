from collections import defaultdict, deque


def solution(n: int, edge: list) -> int:
    # the farthest node from 1
    # the farthest = the largest edges in the shortest moving
    answer = 0
    adj = defaultdict(list)
    for s, e in edge:
        adj[s].append(e)
        adj[e].append(s)
    visited = [0] * n
    queue = deque()
    dist = 0
    queue.append([1, dist])
    visited[0] += 1
    max_d = -1
    while queue:
        n, d = queue.popleft()
        if d > max_d:
            answer = 0
            max_d = d
        if d == max_d:
            answer += 1

        for a in adj[n]:
            if visited[a - 1] == 0:
                queue.append([a, d + 1])
                visited[a - 1] += 1

    return answer