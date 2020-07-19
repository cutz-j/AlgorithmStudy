import sys
sys.setrecursionlimit(10**8)

def dfs(row, col):
    global count, global_count
    visited[row][col] = True
 
    if count == 1:
        global_count += 1
    
    for i in range(4):
        new_row, new_col = row + row_dir[i], col + col_dir[i]
        if (new_row >= 0 and new_row < N) and (new_col >= 0 and new_col < M):
            if visited[new_row][new_col] == False:
                if cabbage[new_row][new_col] == 1:
                    count += 1
                    dfs(new_row, new_col)
                    

def dfs_all():
    global count

    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1:
                if visited[i][j] == False:
                    count = 1
                    dfs(i, j)



rl = input
#rl = lambda: sys.stdin.readline()


T = int(rl())
row_dir = [-1, 0, 1, 0]
col_dir = [0, -1, 0, 1]

for _ in range(T):
    M, N, K = map(int, rl().split())
    location = []
    cabbage = [[0]*M for i in range(N)]
    for __ in range(K):
        x, y = map(int, rl().split())
        cabbage[y][x] = 1
        
    visited = [[False]*M for i in range(N)]
    global_count, count = 0, 1
    dfs_all()
    print(global_count)
    
        
