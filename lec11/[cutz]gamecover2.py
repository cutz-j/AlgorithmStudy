import sys



rl = input
#rl = lambda: sys.stdin.readline()

C = int(rl())

for _ in range(C):
    H,W,R,C = map(int, rl().split())
    game = []
    block = []
    for __ in range(H):
        game.append(map(str, rl().split()))
    
    for ___ in range(R):
        block.append(map(str, rl().split()))
    