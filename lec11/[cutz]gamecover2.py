import sys

def rotate(arr):
    # upper most --> rotation --> relative coordinates
    rotated = []
    for i in range(len(arr)):
        rotated.append([0 for j in range(len(arr[0]))])
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            rotated[i][len(arr)-i-1] = arr[i][j]
            
    return rotated
    
def generate(block):
    for rot in range(4):
        origin_y, origin_x = -1, -1
        
        for i in range(len(block)):
            for j in range(len(block[0])):
                if block[i][j] == 1:
                    if origin_y == -1:
                        origin_y = i
                        origin_x = j
                    rotations[rot].append((i - origin_y, j - origin_x))
        block = rotate(block)
    
    
    
rl = input
#rl = lambda: sys.stdin.readline()

C = int(rl())

for _ in range(C):
    H,W,R,C = map(int, rl().split())
    game = []
    block = []
    for __ in range(H):
        game_row = rl()
        game_tmp = []
        for a in game_row:
            if a == '#':
                game_tmp.append(1)
            else:
                game_tmp.append(0)
        game.append(game_tmp)
    
    for ___ in range(R):
        block_row = rl()
        block_tmp = []
        for b in block_row:
            if b == '#':
                block_tmp.append(1)
            else:
                block_tmp.append(0)
        block.append(block_tmp)
    
    rotations = [[], [], [], []]
