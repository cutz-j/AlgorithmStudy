import sys
from itertools import combinations
import copy
from collections import deque
    

def bfs(res, comb, ans):
    queue = deque()
    virus_num, cnt = inactive, 0
    for row, col in comb:
        queue.append((row, col, cnt))
    
    while queue:
        row, col, cnt = queue.popleft()
        res[row][col] = -1
        if cnt >= ans:
            break
        for k in range(4):
            new_row, new_col = row+row_dir[k], col+col_dir[k]
            if (0 <= new_row < N) and (0 <= new_col < N):
                if res[new_row][new_col] == -1:
                    continue
                
                if res[new_row][new_col] == 0:
                    queue.append((new_row, new_col, cnt+1))
                    virus_num += 1
                    res[new_row][new_col] = -1
      
                elif lab[new_row][new_col] == 2 and virus_num < space:
                    queue.append((new_row, new_col, cnt+1))
                    res[new_row][new_col] = -1
                    

            
            if virus_num == space:
                break

    if virus_num == space:
        if cnt < ans:
            ans = cnt
    return ans

rl = input
# rl = lambda: sys.stdin.readline()

N, M = map(int, rl().split())

row_dir, col_dir = [1, 0, -1, 0], [0, 1, 0, -1]

lab, virus, space, inactive = [], [], 0, 0
for i in range(N):
    row = list(map(int, rl().split()))
    lab.append(row)
    for j, value in enumerate(row):
        if value == 2:
            virus.append((i, j))
            inactive += 1
            space += 1
        elif value == 0:
            space += 1
            
ans = sys.maxsize

if space == inactive:
    answer = 0
    print(answer)
else:
    comb_set = combinations(virus, M)
    answer = sys.maxsize
    for comb in comb_set:
        res = copy.deepcopy(lab)
        ans = bfs(res, comb, ans)
        if ans < answer:
            answer = ans
    if answer == sys.maxsize:
        answer = -1
    print(answer)
    



