import sys
from collections import defaultdict, deque

def dist(shark, size, fish):
    res = defaultdict(list)
    visited = [[False for _ in range(N)] for __ in range(N)]
    queue = deque()
    queue.append((shark[0], shark[1], 0))
    visited[shark[0]][shark[1]] = True
    min_d = sys.maxsize
    while queue:
        y, x, d = queue.popleft()
        if d + 1 > min_d + 2:
            all_map[shark[0]][shark[1]] = 0
            return [(min(res[min_d]), min_d)]
        for i in range(4):
            new_y, new_x = y+row_dir[i], x+col_dir[i]
            if 0 <= new_y < N and 0 <= new_x < N:
                if visited[new_y][new_x] == False:
                    if all_map[new_y][new_x] == 0 or all_map[new_y][new_x] == size:
                        queue.append((new_y, new_x, d+1))
                        visited[new_y][new_x] = True
                    elif 0 < all_map[new_y][new_x] < size:
                        res[d+1].append((new_y, new_x))
                        visited[new_y][new_x]= True
                        if d+1 < min_d:
                            min_d = d+1


    all_map[shark[0]][shark[1]] = 0
    if res:
        return [(min(res[min_d]), min_d)]
    else:
        return res


rl = lambda: sys.stdin.readline()

row_dir, col_dir = [-1, 0, 0, 1], [0, -1, 1, 0]

N = int(rl())
all_map = []
fish = defaultdict(list)
shark_coord, shark_size = (0, 0), 2
for i in range(N):
    row = list(map(int, rl().split()))
    all_map.append(row)
    for j, r in enumerate(row):
        if r:
            if r == 9:
                shark_coord = (i, j)
            else:
                fish[r].append((i,j))


size_cnt, time = 0, 0
while True:
    res = dist(shark_coord, shark_size, fish)
    # print("s_coord", shark_coord, "s_size", shark_size, "fish", res)
    if res:
        y, x = res[0][0]
        fish[(y, x)] = 0
        size_cnt += 1
        if size_cnt == shark_size:
            shark_size += 1
            size_cnt = 0
        all_map[y][x] = 0
        shark_coord = (y, x)
        time += res[0][1]

    else:
        break

print(time)

