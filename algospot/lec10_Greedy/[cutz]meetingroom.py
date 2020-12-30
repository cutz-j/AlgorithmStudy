import sys

def solve():
    count = 0
    last_time = 0
    for s, e in sorted_time:
        if last_time <= s:
            last_time = e
            count += 1
    return count



#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())

time = []
for _ in range(N):
    time.append(list(map(int, rl().split())))
    
time = sorted(time, key=lambda x: x[1])

sorted_time = []
cache = []
last_s, last_e = time[0]
for s, e in time:
    if last_e == e:
        cache.append([s, e])
        last_s, last_e, = s, e
    else:
        cache = sorted(cache, key=lambda x: x[0])
        for s_c, e_c in cache:
            sorted_time.append([s_c, e_c])
        last_s, last_e = s, e
        cache = [[s, e]]
if cache:
    cache = sorted(cache, key=lambda x: x[0])
    for s_c, e_c in cache:
        sorted_time.append([s_c, e_c])
        
print(solve())