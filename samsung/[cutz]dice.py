import sys
import copy

def step(all_map, dice, now, direction):
    new_dice = [0 for i in range(6)]
    if direction == 1:
        new_x, new_y = now[0], now[1]+1
        for i in range(6):
            new_dice[i] = dice[direct[direction-1][i]]

    elif direction == 2:
        new_x, new_y = now[0], now[1]-1
        for i in range(6):
            new_dice[i] = dice[direct[direction-1][i]]

    elif direction == 3:
        new_x, new_y = now[0]-1, now[1]
        for i in range(6):
            new_dice[i] = dice[direct[direction-1][i]]

    elif direction == 4:
        new_x, new_y = now[0]+1, now[1]
        for i in range(6):
            new_dice[i] = dice[direct[direction-1][i]]

    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
        return all_map, dice, now, True
    else:
        if all_map[new_x][new_y] == 0:
            all_map[new_x][new_y] = new_dice[5]
        else:
            new_dice[5] = all_map[new_x][new_y]
            all_map[new_x][new_y] = 0
    return all_map, new_dice, (new_x, new_y), False



rl = lambda: sys.stdin.readline()

N, M, x, y, K = map(int, rl().split())

all_map = []
for _ in range(N):
    all_map.append(list(map(int,rl().split())))

query = list(map(int, rl().split()))

dice = [0, 0, 0, 0, 0, 0] # 위 / 동 / 서 / 북 / 남 / 아래
direct = [(2, 0, 5, 3, 4, 1),
          (1, 5, 0, 3, 4, 2),
          (4, 1, 2, 0, 5, 3),
          (3, 1, 2, 5, 0, 4)]

coord = (x, y)
for q in query:
    all_map, dice, coord, ignore = step(all_map, dice, coord, q)
    # print(dice)
    if ignore:
        continue
    else:
        print(dice[0])