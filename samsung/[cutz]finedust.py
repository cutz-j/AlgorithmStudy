import sys
from collections import defaultdict

def dust_step(dust, A):
    dust_copy = defaultdict(int)
    for y, x in list(dust):
        cnt = 0
        d = dust[(y, x)]
        if d == 0:
            continue
        dust_copy[(y, x)] += d
        for i in range(4):
            new_y, new_x = row_dir[i]+y, col_dir[i]+x
            if 0 <= new_y < R and 0 <= new_x < C:
                if (new_y, new_x) not in air:
                    A[new_y][new_x] += (d // 5)
                    dust_copy[(new_y, new_x)] += (d // 5)
                    cnt += 1
        A[y][x] -= (d // 5) * cnt
        dust_copy[(y, x)] -= (d // 5) * cnt
    return dust_copy, A

def air_step(A, air):
    up, down = air[0][0], air[1][0]
    prev_up, prev_down  = A[up][1], A[down][1]
    A[up][1], A[down][1] = 0, 0
    dust[(up, 1)], dust[(down,1)] = 0, 0
    # up & down
    for i in range(2, C):
        now_up, now_down = A[up][i], A[down][i]
        A[up][i], A[down][i] = prev_up, prev_down
        dust[(up, i)], dust[(down, i)] = prev_up, prev_down
        prev_up, prev_down = now_up, now_down

    # up
    for i in range(up-1, -1, -1):
        now_up = A[i][C-1]
        A[i][C-1] = prev_up
        dust[(i, C-1)] = prev_up
        prev_up = now_up

    # down
    for i in range(down+1, R):
        now_down = A[i][C-1]
        A[i][C-1] = prev_down
        dust[(i, C-1)] = prev_down
        prev_down = now_down

    # up & down
    for i in range(C-2, -1, -1):
        now_up, now_down = A[0][i], A[R-1][i]
        A[0][i], A[R-1][i] = prev_up, prev_down
        dust[(0, i)], dust[(R-1, i)] = prev_up, prev_down
        prev_up, prev_down = now_up, now_down

    # up
    for i in range(1, up-1):
        now_up = A[i][0]
        A[i][0] = prev_up
        dust[(i, 0)] = prev_up
        prev_up = now_up

    # down
    for i in range(R-2, down, -1):
        now_down = A[i][0]
        A[i][0] = prev_down
        dust[(i, 0)] = prev_down
        prev_down = now_down

    return A

rl = lambda: sys.stdin.readline()
row_dir, col_dir = [1, 0, -1, 0], [0, 1, 0, -1]


R, C, T = map(int, rl().split())
A = []
dust = defaultdict(int)
air = []

for i in range(R):
    row = list(map(int, rl().split()))
    A.append(row)
    for j, r in enumerate(row):
        if r == -1:
            air.append((i, j))

        elif r != 0:
            dust[(i, j)] = r

air = sorted(air)
time = 0
while time < T:
    # print("before")
    # for a in A:
    #     print(a)
    # print()
    # print(dust)
    dust, A = dust_step(dust, A)
    # print("dust")
    # for a in A:
    #     print(a)
    # print(dust)
    A = air_step(A, air)
    time += 1

ans = 0
for i in range(R):
    for j in range(C):
        ans += A[i][j]

print(ans+2)

