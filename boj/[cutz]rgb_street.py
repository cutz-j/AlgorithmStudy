import sys
from collections import defaultdict

rl = lambda: sys.stdin.readline()

N = int(rl())
price = []
for _ in range(N):
    price.append(list(map(int, rl().split())))

cache = defaultdict(list)

for i in range(N):
    cache[i] = [-1, -1, -1]
    if i == 0:
        cache[i] = price[i]
        continue

    cache[i][0] = price[i][0] + min(cache[i-1][1], cache[i-1][2])
    cache[i][1] = price[i][1] + min(cache[i-1][0], cache[i-1][2])
    cache[i][2] = price[i][2] + min(cache[i-1][0], cache[i-1][1])

answer = min(cache[i])
print(answer)

