import sys
from itertools import combinations
import copy

def step(virus_map, start, cnt):
    res = copy.deepcopy(virus_map)
    virus_num = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 1:
                continue
            elif lab[i][j] == 2:
                if (i, j) not in start:
                    continue
        
            value = virus_map[i][j]
            if value == 1:
                for k in range(4):
                    new_row, new_col = i+row_dir[k], j+col_dir[k]
                    if (0 <= new_row < N) and (0 <= new_col < N):
                        if res[new_row][new_col] == 0:
                            if lab[new_row][new_col] != 1 and lab[new_row][new_col] != 2:
                                res[new_row][new_col] = 1
                                virus_num += 1
        
    return res, cnt+1, virus_num



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
for comb in combinations(virus, M):
    virus_num, cnt = 0, 0
    virus_map = [[0]*N for _ in range(N)]
    for row, col in comb:
        virus_map[row][col] = 1
        virus_num += 1
    
    while True:
        virus_map, cnt, v_num = step(virus_map, comb, cnt)
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



