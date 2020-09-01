import sys
from itertools import combinations
import copy

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
    

def bfs():
    ans = sys.maxsize
    comb_set = combinations(virus, M)
    for comb in comb_set:
        queue = Queue()
        res = copy.deepcopy(lab)
        virus_num, cnt = inactive, 0
        for row, col in comb:
            res[row][col] = -1
            queue.append((row, col, cnt))
        
        while queue.empty() == False:
            row, col, cnt = queue.pop()
            if cnt > ans:
                break
            for k in range(4):
                new_row, new_col = row+row_dir[k], col+col_dir[k]
                if (0 <= new_row < N) and (0 <= new_col < N):
                    if res[new_row][new_col] == 0:
                        queue.append((new_row, new_col, cnt+1))
                        virus_num += 1
                        res[new_row][new_col] = -1
                        
                    elif res[new_row][new_col] == 2 and virus_num < space:
                        queue.append((new_row, new_col, cnt+1))
                        res[new_row][new_col] = -1
 
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

if space == inactive:
    ans = 0
    print(ans)

else:
    ans = bfs()
    if ans == sys.maxsize:
        ans = -1
    print(ans)



