import sys
from collections import defaultdict

rl = lambda: sys.stdin.readline()
# n: length of wine
N = int(rl())
wine = []
for _ in range(N):
    wine.append(int(rl()))

cache = defaultdict(int)

if len(wine) == 1:
    cache[0] = wine[0]

elif len(wine) == 2:
    cache[0] = wine[0]
    cache[1] = wine[0]+wine[1]

else:
    cache[0] = wine[0]
    cache[1] = wine[0]+wine[1]
    cache[2] = max(wine[0]+wine[2], wine[1]+wine[2], cache[1])

    for i in range(3, len(wine)):
        cache[i] = max(cache[i-2]+wine[i], cache[i-3]+wine[i-1]+wine[i], cache[i-1])

print(cache[N-1])