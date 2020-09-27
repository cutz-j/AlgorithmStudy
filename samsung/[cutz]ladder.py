import sys
from itertools import combinations
# from collections import defaultdict
# N: int / row /  2 <= N <= 10
# M: int / col / 1 <= M <= (N-1)*H
# H: int / 후보 / 1 <= H <= 30

def ladder(n: int, h: int, adj: list) -> bool:
    for i in range(n):
        a, b = 0, i
        while a < h:
            if adj.get((a, b), None):
                a, b = adj[(a,b)]
            a += 1
        if b != i:
            return False
    return True


rl = lambda: sys.stdin.readline()

N, M, H = map(int, rl().split())z

adj = {} # last N-1 is invert direction // bi-drection
for _ in range(M):
    a, b = map(int, rl().split())
    adj[(a-1, b-1)] = (a-1, b)
    adj[(a-1, b)] = (a-1, b-1)

all_list = []
for i in range(H):
    for j in range(N-1):
        if adj.get((i, j), None):
            continue
        all_list.append((i, j))

# exhastive search
answer, stop = -1, False
for i in range(0, 4):
    comb = combinations(all_list, i)
    for c in comb: # all possible cases <= 3
        adj_copy = {a: b for a, b in adj.items()} # copy
        for a, b in c:
            adj_copy[(a, b)] = (a, b+1)
            adj_copy[(a, b+1)] = (a, b)
        if ladder(N, H, adj_copy):
            stop = True
            break
    if stop:
        answer = i
        break

print(answer)