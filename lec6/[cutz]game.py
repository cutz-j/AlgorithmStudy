import sys
sys.setrecursionlimit(100000)

def game(y, x, cnt): # 완전탐색 --> 재귀초과(무한번 케이스)
    if cnt > 100:
        return -1
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
    
def game_dp(y, x):
    if y >= N or y < 0 or x >= M or x < 0 or state[y][x] == 'H':
        return 0
    if visited[y][x]:
        print(-1)
        exit(0)
        
    if cache.get((y, x), 0) != 0:
        return cache[(y, x)]
    
    visited[y][x] = True
    for i in range(4):
        value = int(state[y][x])
        ny = y + value * dy[i]
        nx = x + value * dx[i]
        cache[(y, x)] = max(cache.get((y, x), 0), game_dp(ny,nx)+1)
    visited[y][x] = False
    
    return cache[(y, x)]
    
    
    
    
    
#rl = lambda: sys.stdin.readline()
rl = input

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
N, M = map(int, rl().split())
state = []
for _ in range(N):
    row = rl()
    row_list = []
    for letter in row:
        row_list.append(letter)
    state.append(row_list)
cache = {}
visited = [[False]*M for _ in range(N)]
print(game_dp(0, 0))
