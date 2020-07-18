import sys

def dfs(row, col):
    global house_count, count
    visited[row][col] = True
    
    if count == 1:
        house_count += 1
    
    for i in range(4):
        new_row, new_col = row+row_dir[i], col+col_dir[i]
        if (new_row >= 0 and new_row < N) and (new_col >= 0 and new_col < N):
            if int(adj[new_row][new_col]) == 1:
                if visited[new_row][new_col] == False:
                    
                    count += 1
                    dfs(new_row, new_col)
            

def dfs_all():
    global count
    cnt_list = []
    for i in range(N):
        for j in range(N):
            if int(adj[i][j]) == 1:
                if visited[i][j] == False:
                    count = 1
                    dfs(i, j)
                    cnt_list.append(count)
    return cnt_list
    
rl = input
#rl = lambda: sys.stdin.readline()

N = int(rl())
adj = []
for _ in range(N):
    adj.append(rl())
    
visited = [[False] * N for _ in range(N)]
house_count = 0
row_dir, col_dir = [-1, 0, 1, 0], [0, -1, 0, 1]

cnt_list = dfs_all()
cnt_list.sort()
print(house_count)
for c in cnt_list:
    print(c)

