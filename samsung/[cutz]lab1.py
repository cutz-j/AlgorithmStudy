import sys
from itertools import combinations

class Queue():
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.list = []
        self.pop_count = 0

    def append(self, x):
        self.list.append(x)
        self.rear += 1

    def pop(self):
        res = self.list[self.front]
        self.front += 1
        self.pop_count += 1
        return res

    def empty(self):
        return len(self.list) == self.pop_count


res = 0
rl = lambda: sys.stdin.readline()

N, M = map(int, rl().split())
all_map = []
virus = []
zero = []
virus_num = sys.maxsize
for i in range(N):
    tmp = list(map(int, rl().split()))
    for j, v in enumerate(tmp):
        if v == 2:
            virus.append((i, j))
        elif v == 0:
            zero.append((i, j))
    all_map.append(tmp)

row_dir, col_dir = [1, 0, -1, 0], [0, 1, 0, -1]

wall_comb = combinations(zero, 3)
for wall in wall_comb:
    # visited = copy.deepcopy(all_map)
    visited = []
    for i in range(N):
        tmp = []
        for j in range(M):
            tmp.append(all_map[i][j])
        visited.append(tmp)

    for w in wall:
        visited[w[0]][w[1]] = 1
    v_num = 0
    queue = Queue()
    for v in virus:
        queue.append(v)

    while queue.empty() == False:
        r, c = queue.pop()
        v_num += 1
        if v_num > virus_num:
            break

        for i in range(4):
            new_r, new_c = r + row_dir[i], c + col_dir[i]
            if (0 <= new_r < N) and (0 <= new_c < M):
                if visited[new_r][new_c] == 0:
                    queue.append((new_r, new_c))
                    visited[new_r][new_c] = 2

    cnt, v_cnt = 0, 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                cnt += 1
            if visited[i][j] == 2:
                v_cnt += 1

    if cnt > res:
        res = cnt
        virus_num = v_cnt

print(res)