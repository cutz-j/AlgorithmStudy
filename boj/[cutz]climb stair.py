import sys
from collections import defaultdict

rl = lambda: sys.stdin.readline()

# stair length
length = int(rl())
stair = []
for i in range(length):
    stair.append(int(rl()))

cache = defaultdict(int)

if len(stair)==1:
    cache[0] = stair[0]

elif len(stair) == 2:
    cache[0] = stair[0]
    cache[1] = max(cache[0]+stair[1], stair[1])

else:
    cache[0] = stair[0]
    cache[1] = max(stair[0]+stair[1], stair[1])
    cache[2] = max(stair[0]+stair[2], stair[1]+stair[2])

    for i in range(3, len(stair)):
        cache[i] = max(cache[i-2]+stair[i], cache[i-3]+stair[i-1]+stair[i])

print(cache[len(stair)-1])
