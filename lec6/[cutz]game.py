import sys

def game(y, x, cnt): # 완전탐색 --> 재귀초
    if y < 0 or y >= N:
        return cnt
    elif x < 0 or x >= M:
        return cnt
    elif state[y][x] == 'H':
        return cnt
    else:
        X = int(state[y][x])
        right = game(y, x+X, cnt+1) # right
        bottom = game(y+X, x, cnt+1) # bottom
        left = game(y, x-X, cnt+1) # left
        top = game(y-X, x, cnt+1) # top
        return max([right, bottom, left, top])
    
#rl = lambda: sys.stdin.readline()
rl = input

N, M = map(int, rl().split())
state = []
for _ in range(N):
    row = rl()
    row_list = []
    for letter in row:
        row_list.append(letter)
    state.append(row_list)
print(game(0, 0, 0))
