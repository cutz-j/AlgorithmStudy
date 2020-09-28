import sys

rl = lambda: sys.stdin.readline()

direction = {0:(0, 1), 1:(-1, 0), 2:(0, -1), 3:(1, 0)}
ans = 0

all_map = [[0 for i in range(101)] for j in range(101)]
dragon = []
N = int(rl())

for _ in range(N):
    dragon.append((map(int, rl().split())))

for x, y, d, g in dragon:
    all_map[y][x] = 1
    line = 0
    stack = [d]
    y, x = y + direction[d][0], x + direction[d][1]
    all_map[y][x] = 1
    line += 1
    while line <= g:
        tmp_stack = stack[:]
        new_stack = []
        while stack:
            old_d = stack.pop()
            d = old_d + 1
            if d == 4:
                d = 0
            y, x = y + direction[d][0], x + direction[d][1]
            new_stack.append(d)
            all_map[y][x]= 1
        stack = tmp_stack[:] + new_stack[:]
        line += 1


for i in range(100):
    for j in range(100):
        if all_map[i][j] and all_map[i][j+1] and all_map[i+1][j] and all_map[i+1][j+1]:
            ans +=1

print(ans)
