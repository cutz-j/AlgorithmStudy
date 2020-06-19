import sys


def dp():
    cache = {}
    cache[0] = (1, 0)
    cache[1] = (0, 1)
    cache[2] = (1, 1)
    
    for i in range(3, 41):
        cache[i] = (cache[i-1][0] + cache[i-2][0], cache[i-1][1] + cache[i-2][1])
    
    return cache

#rl = lambda: sys.stdin.readline()
rl = input
cache = dp()
T = int(rl())
for _ in range(T):
    answer = cache[int(rl())]
    print('{} {}'.format(answer[0], answer[1]))