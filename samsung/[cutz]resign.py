import sys

def step(t, r):
    global res
    # if cache.get(t, -1) != -1:
    #     return cache[t]
    if t >= N:
        return r

    for j in range(t, N):
        if j+time[j] <= N:
            # cache[j] = max(step(j+time[j], r+reward[j]), cache.get(j, 0))
            result = step(j+time[j], r+reward[j])
            if result > res:
                res = result
    return r

rl = lambda: sys.stdin.readline()

N = int(rl())
time, reward = [], []
for _ in range(N):
    t, p = map(int, rl().split())
    time.append(t)
    reward.append(p)

res = 0
cache = {}
step(0, 0)
print(res)
# if cache:
#     print(max(cache.values()))
# else:
#     print(0)
