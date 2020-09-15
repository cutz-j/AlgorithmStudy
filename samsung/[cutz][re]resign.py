import sys

def step(t, r):
    if cache.get(t, -1) != -1:
        return cache[t]

    if t >= N:
        return r

    for j in range(t, N):
        if j+time[j] <= N:
            cache[j] = max(step(j+time[j], r+reward[j]), cache.get(j, 0))
        else:
            cache[j] = r
    return r


rl = lambda: sys.stdin.readline()

N = int(rl())
time, reward = [], []
for _ in range(N):
    t, p = map(int, rl().split())
    time.append(t)
    reward.append(p)
# visited = [-1 for _ in range(N)]
cache = {}
step(0, 0)
if cache:
    print(max(cache.values()))
else:
    print(0)