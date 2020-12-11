import sys

def step(r, c, d):
    # for a in all_map:
    #     print(a)
    # print()
    global cnt, end
    clean = False
    for i in range(1, 5):
        new_idx = d + i
        if new_idx >= 4:
            new_idx -= 4
        new_row, new_col = r+row_dir[new_idx], c+col_dir[new_idx]
        if 0 <= new_row < N and 0 <= new_col < M:
            if all_map[new_row][new_col] == 0:
                all_map[new_row][new_col] = 2
                clean = True
                cnt += 1
                break
    if clean == False:
        new_idx = d + 2
        if new_idx >= 4:
            new_idx -= 4
        new_row, new_col = r+row_dir[new_idx], c+col_dir[new_idx]
        if 0 <= new_row < N and 0 <= new_col < M:
            if all_map[new_row][new_col] == 1:
                end = True
            else:
                new_idx = d
        else:
            end = True
    return new_row, new_col, new_idx

rl = lambda: sys.stdin.readline()

N, M = map(int, rl().split())
r, c, d = map(int, rl().split())
all_map = []
for _ in range(N):
    all_map.append(list(map(int, rl().split())))

row_dir, col_dir = [0, 1, 0, -1], [-1, 0, 1, 0]
query_dict = {0:3, 1:2, 2:1, 3:0}

all_map[r][c] = 2
cnt = 1
d = query_dict[d]
end = False

while end == False:
    r, c, d = step(r, c, d)
    # print(r, c, d)

print(cnt)