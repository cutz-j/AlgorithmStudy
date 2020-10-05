import sys
from collections import defaultdict

# search: O(n^2) / move: O(n)

def move():
    new_map = [[False for _ in range(C)] for __ in range(R)]
    new_shark = {}

    for (r, c) in list(shark):
        s, d, z = shark[(r, c)]
        all_map[r][c] = False
        s_copy = s
        if d == 1: # up
            s -= r
            if s > 0:
                d = 2
            change, div = divmod(s, R-1)
            if change % 2 == 0:
                new_r, new_c = div, c
            else:
                new_r, new_c = R-div-1, c
                if div:
                    d = 1
        elif d == 2: # down
            s -= (R-r-1)
            if s > 0:
                d = 1
            change, div = divmod(s, R-1)
            if change % 2 == 0:
                new_r, new_c = R-div-1, c
            else:
                new_r, new_c = div, c
                if div:
                    d = 2
        elif d == 3: # right
            s -= (C-c-1)
            if s > 0:
                d = 4
            change, div = divmod(s, C-1)
            if change % 2 == 0:
                new_r, new_c = r, C-div-1
            else:
                new_r, new_c = r, div
                if div:
                    d = 3

        elif d == 4:
            s -= c
            if s > 0:
                d = 3
            change, div = divmod(s, C-1)
            if change % 2 == 0:
                new_r, new_c = r, div
            else:
                new_r, new_c = r, C-div-1
                if div:
                    d = 4

        if new_map[new_r][new_c]:
            prev_z = new_shark[(new_r,new_c)][2]
            if z > prev_z:
                new_shark[(new_r,new_c)] = (s_copy, d, z)
                new_map[new_r][new_c] = True
        else:
            new_map[new_r][new_c] = True
            new_shark[(new_r,new_c)] = (s_copy,d,z)
        # print((r, c), (new_r, new_c))

    return new_shark, new_map

def fish(col):
    global answer
    for i in range(R):
        if all_map[i][col]:
            # print(shark[(i, col)])
            all_map[i][col] = False
            size = shark[(i, col)][2]
            answer += size
            del shark[(i, col)]
            return


rl = lambda: sys.stdin.readline()
shark = defaultdict(tuple)
R, C, M = map(int, rl().split())
all_map = [[False for _ in range(C)] for __ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, rl().split())
    shark[(r-1, c-1)] = (s, d, z)
    all_map[r-1][c-1] = True

answer = 0
for i in range(C):
    fish(i)
    shark, all_map = move()
    # for a in all_map:
    #     print(a)
    # print(shark)

print(answer)
