import sys



rl = int
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
    
    