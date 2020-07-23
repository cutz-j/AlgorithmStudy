import sys

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
    global zero_cnt
    result = 0
    while que.empty() == False:
        row, col = que.pop()
        
        for i in range(4):  
             new_row, new_col = row+row_dir[i], col+col_dir[i]
             if (new_row >= 0 and new_row < N) and (new_col >= 0 and new_col < M):
                 tmp = tomato[row][col] + 1
                 if tomato[new_row][new_col] == 0:
                     que.append((new_row, new_col))
                     tomato[new_row][new_col] = tmp
                     zero_cnt -= 1
                     if tmp > result:
                         result = tmp
                   
    if result == 0:
        result = 1
    if zero_cnt != 0:
        result = 0
    return result - 1
    
    

rl = input
# rl = lambda: sys.stdin.readline()

M, N = map(int, rl().split())

row_dir = [-1, 0, 1, 0]
col_dir = [0, -1, 0, 1]
zero_cnt = 0

tomato, que = [], Queue()
for i in range(N):
    row_list = list(map(int, rl().split()))
    tomato.append(row_list)
    for j in range(len(tomato[i])):
        if tomato[i][j] == 1:
            que.append((i, j))
        if tomato[i][j] == 0:
            zero_cnt += 1

print(bfs())