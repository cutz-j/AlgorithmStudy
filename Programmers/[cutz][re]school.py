from collections import defaultdict


def solution(m, n, puddles):
    answer = defaultdict(int)

    answer[(1, 1)] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            if [j, i] in puddles:
                answer[(i, j)] = 0
            else:
                answer[(i, j)] = answer[(i - 1, j)] + answer[(i, j - 1)]

    return answer[(n, m)] % 1000000007