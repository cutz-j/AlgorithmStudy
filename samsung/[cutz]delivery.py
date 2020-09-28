import sys
from itertools import combinations

# Exhaustive search
rl = lambda: sys.stdin.readline()

N, M = map(int, rl().split())

chicken, house = [], []

for i in range(N):
    row = list(map(int, rl().split()))
    for j, r in enumerate(row):
        if r == 1:
           house.append((i, j))
        elif r == 2:
            chicken.append((i, j))

comb = combinations(chicken, M)
ans = sys.maxsize
for c in comb:
    # O(CH)
    all_dist = 0
    # chicken dist for each house
    for h in house:
        d = sys.maxsize
        for ch in c:
            dist = abs(ch[0] - h[0]) + abs(ch[1] - h[1])
            if dist < d:
                d = dist
        all_dist += d
    if all_dist < ans:
        ans = all_dist

print(ans)