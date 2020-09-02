import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append([red, blue])
    visited = [[[0 for _ in range(N)] for __ in range(M)] for ___ in range(2)]
    step = 0
    while queue:
        (red_x, red_y), (blue_x, blue_y) = queue.popleft()
        visited[0][red_x][red_y] = 1
        visited[1][blue_x][blue_y] = 1
        for i in range(4):
            red_f, blue_f = False, False
            red_o, blue_o = False, False
            while not red_f and blue_f:
                if not red_f:
                    new_red_row, new_red_col = red_x+row_dir[i], red_y+col_dir[i]
                if not blue_f:
                    new_blue_row, new_blue_col = blue_x+row_dir[i], blue_y+col_dir[i]
                
                if gmap[new_red_row][new_red_col] == '#' and not red_f:
                    res_red_row, res_red_col = new_red_row-row_dir[i], new_red_col-col_dir[i]
                    red_f = True
                
                if gmap[new_blue_row][new_blue_col] == '#' and not blue_f:
                    res_blue_row, res_blue_col = new_blue_row-row_dir[i], new_blue_col-col_dir[i]
                    blue_f = True
                    
                if gmap[new_red_row][new_red_col] == 'O' and not red_f:
                    red_o = True
                    red_f = True
                    
                if gmap[new_blue_row][new_blue_col] == 'O' and not blue_f:
                    blue_o = True
                    blue_f = True


rl = input
# rl = lambda: sys.stdin.readline()

N, M = map(int, rl().split())
gmap = []
for i in range(N):
    row = list(rl())
    gmap.append(row)
    for j, value in enumerate(row):
        if value == 'R':
            red = (i, j)
        elif value == 'B':
            blue = (i, j)
        elif value == 'O':
            out = (i, j)
 

row_dir, col_dir = [1, 0, -1, 0], [0, 1, 0, -1]



    