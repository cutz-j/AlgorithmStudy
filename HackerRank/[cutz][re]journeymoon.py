#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
sys.setrecursionlimit(9999999)

def dfs(i):
    global arr
    visited[i] = 1
    arr.append(i)
    for j in astronaut.get(i, []):
        if visited[j] == 0:
            dfs(j)


def dfsall():
    global arr
    group = []
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            group.append(len(arr))
            arr = []
    return group
    


# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    group = dfsall()
    answer = 0
    length = len(group)
    all_sum = sum(group)
    res = []
    for g in group:
        if g == 1:
            answer += all_sum-1
            all_sum -= 1
        else:
            res.append(g)
    comb = combinations(range(len(res)), 2)
    for c1, c2 in comb:
        answer += res[c1]*res[c2]
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rl = lambda: sys.stdin.readline()
    np = rl().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = {}
    for _ in range(p):
        s, e = map(int, rl().split())
        if astronaut.get(s, []):
            astronaut[s].append(e)
        else:
            astronaut[s] = [e]
        if astronaut.get(e, []):
            astronaut[e].append(s)
        else:
            astronaut[e] = [s]

    visited = [0 for _ in range(n)]
    arr = []
    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
