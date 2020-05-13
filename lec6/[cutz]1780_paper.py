import sys




#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())

mat = []
for i in range(N):
    mat.append(list(map(int, rl().split(' '))))