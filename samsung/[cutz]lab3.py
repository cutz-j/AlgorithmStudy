import sys
from itertools import combinations
import copy

def step(virus_map, start, cnt):
    res = copy.deepcopy(virus_map)
    virus_num, virus_list = 0, []
    
    for row, col in start:
        for k in range(4):
            new_row, new_col = row+row_dir[k], col+col_dir[k]
            if (0 <= new_row < N) and (0 <= new_col < N):
                if res[new_row][new_col] == 0:
                    if lab[new_row][new_col] != 1 and lab[new_row][new_col] != 2:
                        res[new_row][new_col] = 1
                        virus_num += 1
                        virus_list.append((new_row, new_col))
    return res, cnt+1, virus_num, virus_list


rl = input
# rl = lambda: sys.stdin.readline()

N, M = map(int, rl().split())

row_dir, col_dir = [1, 0, -1, 0], [0, 1, 0, -1]

lab, virus, space = [], [], 0
for i in range(N):
    row = list(map(int, rl().split()))
    lab.append(row)
    for j, value in enumerate(row):
        if value == 2:
            virus.append((i, j))
        elif value == 0:
            space += 1
space += M

ans = sys.maxsize
comb_set = combinations(virus, M)
for comb in comb_set:
    start = []
    virus_num, cnt = 0, 0
    virus_map = [[0]*N for _ in range(N)]
    for row, col in comb:
        virus_map[row][col] = 1
        virus_num += 1
        start.append((row, col))
    
    while True:
        virus_map, cnt, v_num, start = step(virus_map, start, cnt)
        virus_num += v_num
        if virus_num == space:
            if cnt < ans:
                ans = cnt
            break
        if v_num == 0:
            break
        if cnt > ans:
            break



if ans == sys.maxsize:
    ans = -1
if space == M:
    ans = 0
print(ans)



