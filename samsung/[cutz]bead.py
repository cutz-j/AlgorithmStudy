import sys
from collections import deque

def bfs():
    queue = deque()
    ans, step = sys.maxsize, 1
    queue.append([red, blue, step])
    visited = [[[0 for _ in range(M)] for __ in range(N)] for ___ in range(2)]
    while queue:
        (red_x, red_y), (blue_x, blue_y), step = queue.popleft()
        print("red", red_x, red_y, "blue", blue_x, blue_y)
    
        visited[0][red_x][red_y] = 1
        visited[1][blue_x][blue_y] = 1
        
        for i in range(4):
            new_red_row, new_red_col = red_x, red_y
            new_blue_row, new_blue_col = blue_x, blue_y
            red_f, blue_f = False, False
            red_o, blue_o = False, False
            red_step, blue_step = 0, 0
            while not red_f or not blue_f:
                if not red_f:
                    new_red_row, new_red_col = new_red_row+row_dir[i], new_red_col+col_dir[i]
                    red_step += 1
                if not blue_f:
                    new_blue_row, new_blue_col = new_blue_row+row_dir[i], new_blue_col+col_dir[i]
                    blue_step += 1
                
                if gmap[new_red_row][new_red_col] == '#' and not red_f:
                    res_red_row, res_red_col = new_red_row-row_dir[i], new_red_col-col_dir[i]
                    red_f = True
                
                if gmap[new_blue_row][new_blue_col] == '#' and not blue_f:
                    res_blue_row, res_blue_col = new_blue_row-row_dir[i], new_blue_col-col_dir[i]
                    blue_f = True
                    
                if gmap[new_red_row][new_red_col] == 'O' and not red_f:
                    res_red_row, res_red_col = new_red_row, new_red_col
                    red_o = True
                    red_f = True
                    
                if gmap[new_blue_row][new_blue_col] == 'O' and not blue_f:
                    res_blue_row, res_blue_col = new_blue_row, new_blue_col
                    blue_o = True
                    blue_f = True
                
            if (res_red_row, res_red_col) == (res_blue_row, res_blue_col):
                if red_step < blue_step:
                    res_blue_row, res_blue_col = res_blue_row-row_dir[i], res_blue_col-col_dir[i]
                elif red_step > blue_step:
                    res_red_row, res_red_col = res_red_row-row_dir[i], res_red_col-col_dir[i]
            
            if red_o and not blue_o:
                if step < ans:
                    ans = step
            elif not red_o and not blue_o:
                if (red_x, red_y, blue_x, blue_y) != (res_red_row, res_red_col, res_blue_row, res_blue_col):
                    if visited[0][res_red_row][res_red_col] == 0 or visited[1][res_blue_row][res_blue_col] == 0:
                        queue.append([(res_red_row, res_red_col), (res_blue_row, res_blue_col), step+1])
                    
    if ans > 10 or ans == sys.maxsize:
        ans = -1
    return ans


rl = input
# rl = lambda: sys.stdin.readline()

N, M = map(int, rl().split())
gmap = []
for i in range(N):
    row = list(rl().strip())
    gmap.append(row)
    for j, value in enumerate(row):
        if value == 'R':
            red = (i, j)
        elif value == 'B':
            blue = (i, j)
        elif value == 'O':
            out = (i, j)
 

row_dir, col_dir = [1, 0, -1, 0], [0, 1, 0, -1]
print(bfs())

    