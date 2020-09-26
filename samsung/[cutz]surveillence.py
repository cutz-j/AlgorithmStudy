import sys
from itertools import product

def draw(all_map, rc, num, direct):
    r, c = rc[0], rc[1]
    d = direction[num][direct-1]
    # direction 조합
    for i in range(len(d)):
        new_r, new_c = r, c
        y, x = d[i]
        while True:
            new_r += y
            new_c += x
            if 0 <= new_r < N and 0 <= new_c < M:
                if all_map[new_r][new_c] == 0:
                    all_map[new_r][new_c] = -1
                elif all_map[new_r][new_c] == 6:
                    break
            else:
                break
    return all_map


def solve(all_map, prod):
    global res


    for count in prod:
        # copy
        res_map = []
        for i in range(N):
            tmp = []
            for j in range(M):
                tmp.append(all_map[i][j])
            res_map.append(tmp)

        for idx, c in enumerate(count):
            if c:
                res_map = draw(res_map, cctv[idx][1], cctv[idx][0], c)
        cnt = 0
        for i in range(N):
            # print(res_map[i])
            for j in range(M):
                if res_map[i][j] == 0:
                    cnt += 1
        # print()
        if cnt < res:
            res = cnt


rl = lambda: sys.stdin.readline()
one_direction = [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]] # R B L T
two_direction = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]] # R L / B T
three_direction = [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]]
four_direction = [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], # LTR / TRB
                   [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]] # RBL / BLT
five_direction = [[(0, 1), (1, 0), (0, -1), (-1, 0)]]

direction = {1:one_direction, 2:two_direction, 3:three_direction, 4:four_direction, 5:five_direction}


all_map = []
cctv = []
N, M = map(int, rl().split())
count_map = {1:4, 2:2, 3:4, 4:4, 5:1}

for i in range(N):
    row = list(map(int, rl().split()))
    all_map.append(row)
    for j, r in enumerate(row):
        if r == 1 or r == 2 or r == 3 or r == 4 or r == 5:
            cctv.append([r, (i, j)])

count = []
for r, _ in cctv:
    c = count_map[r]
    tmp = []
    for i in range(c, 0, -1):
        tmp.append(i)
    count.append(tmp)

prod = product(*count)
res = sys.maxsize
solve(all_map, prod)
print(res)