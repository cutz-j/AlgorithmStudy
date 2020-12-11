import sys
from collections import deque

rl = lambda:sys.stdin.readline()

def step(all_map, head, body, direction=3):
    survive = True
    if direction == 0: # 우
        next_y, next_x = head[0], head[1]+1
    elif direction == 1: # 하
        next_y, next_x = head[0]+1, head[1]
    elif direction == 2: # 좌
        next_y, next_x = head[0], head[1]-1
    elif direction == 3: # 상
        next_y, next_x = head[0]-1, head[1]


    if next_y < 0 or next_x < 0 or next_y >= N or next_x >=N:
        survive = False
    else:
        if all_map[next_y][next_x] == 1:
            survive = False

        elif all_map[next_y][next_x] == 2:
            all_map[next_y][next_x] = 1
            body.append((next_y, next_x))

        else:
            all_map[next_y][next_x] = 1
            tmp = body.popleft()
            all_map[tmp[0]][tmp[1]] = 0
            body.append((next_y, next_x))

    return all_map, (next_y, next_x), body, survive

N = int(rl())
K = int(rl())
all_map = [[0 for i in range(N)] for j in range(N)]
apple = {}
for _ in range(K):
    y, x = map(int, rl().split())
    all_map[y-1][x-1] = 2

L = int(rl())
direction = []
for _ in range(L):
    x, c = rl().split()
    direction.append((int(x), c))

all_map[0][0] = 1
sec, time_idx = 0, 0
x, c = direction[time_idx]
survive = True
direc = 0
head, body = (0, 0), deque()
body.append((0, 0))
while survive:
    if sec == x:
        if c == 'D':
            direc += 1
            if direc == 4:
                direc = 0
        else:
            direc -= 1
            if direc == -1:
                direc = 3
        time_idx += 1
        if time_idx < len(direction):
            x, c = direction[time_idx]
        else:
            x = -1

    all_map, head, body, survive = step(all_map, head, body, direc)
    # print(survive, head, body)
    # for a in all_map:
    #     print(a)
    # print()
    sec += 1

print(sec)

