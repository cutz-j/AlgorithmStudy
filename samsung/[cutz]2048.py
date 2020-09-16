import sys
import copy

def change(arr):
    previous = -1
    res = [0 for i in range(N)]
    union = [False for i in range(N)]
    for i, a in enumerate(arr):
        if a == 0:
            res[i] = 0
            continue
        if a == res[previous] and previous != -1 and union[previous] == False:
            res[previous] += a
            union[previous] = True
        elif a == res[previous] and union[previous]:
            res[previous+1] = a
            previous += 1
        elif a != res[previous]:
            res[previous+1] = a
            previous += 1
    return res


def step(board, direction):
    b = copy.deepcopy(board)
    # 상
    if direction == 0:
        for i in range(N):
            col = []
            for j in range(N):
                col.append(b[j][i])
            res = change(col)
            for j in range(N):
                b[j][i] = res[j]
    # 하
    if direction == 1:
        for i in range(N):
            col = []
            for j in range(N):
                col.append(b[j][i])
            res = change(col)
            for j in range(N):
                b[j][i] = res[::-1][j]
    # 좌
    if direction == 2:
        for i in range(N):
            col = b[i]
            res = change(col)
            b[i] = res

    if direction == 3:
        for i in range(N):
            col = b[i]
            res = change(col)
            b[i] = res[::-1]
    return b


def dfs(k, board):
    global res
    for i in range(N):
        for j in range(N):
            if res < board[i][j]:
                res = board[i][j]

    if k == 5:
        return

    for i in range(4):
        dfs(k+1, step(board, i))

rl = lambda: sys.stdin.readline()

N = int(rl())
board = []
for _ in range(N):
    board.append(list(map(int, rl().split())))

res = 0
dfs(0, board)
print(res)