from collections import defaultdict


def solution(triangle):
    answer = 0
    cache = defaultdict(int)
    cache[(0, 0)] = triangle[0][0]

    for i, row in enumerate(triangle[:-1]):
        for j, v in enumerate(row):
            cache[(i + 1, j)] = max(cache[(i, j)] + triangle[i + 1][j], cache[(i + 1, j)])
            cache[(i + 1, j + 1)] = max(cache[(i, j)] + triangle[i + 1][j + 1], cache[(i + 1, j + 1)])

    for i in range(len(triangle) - 1):
        v = cache[(len(triangle) - 1, i)]
        if v > answer:
            answer = v
    return answer