import sys
from itertools import permutations

def hit(bat, base):
    score = 0
    new_base = [0,0,0]
    for i, b in enumerate(base):
        if b == 1:
            if i+bat < 3:
                new_base[i+bat] = 1
            else:
                score += 1
    new_base[bat-1] = 1
    return new_base, score


def inning(start, batters, order):
    out = 0
    base = [0, 0, 0]
    score = 0
    while out != 3:
        if start == 3:
            bat = batters[0]
        elif start > 3:
            bat = batters[order[start-1]]
        else:
            bat = batters[order[start]]
        start += 1
        if start >= 9:
            start = 0
        
        if bat == 0:
            out += 1
        elif bat == 1:
            base, s = hit(bat, base)
            score += s
        elif bat == 2:
            base, s = hit(bat, base)
            score += s
        elif bat == 3:
            base, s = hit(bat, base)
            score += s
        else:
            runner = 0
            for b in base:
                if b == 1:
                    runner += 1
            score += 1 + runner
            runner = 0
            base = [0, 0, 0]
    return start, score


rl = input
# rl = lambda: sys.stdin.readline()

N = int(rl())
info = []
for _ in range(N):
    tmp = list(map(int, rl().split()))
    info.append(tmp)

# time over
order = [1, 2, 3, 4, 5, 6, 7, 8]
all_set = permutations(order)
best_score = 0
for p in all_set:
    score = 0
    start = 0
    for inn in info:
        start, s = inning(start, inn, p)
        score += s
    if score > best_score:
        best_score = score
print(best_score)
    