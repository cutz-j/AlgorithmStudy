import sys

def rotate(arr):
    # upper most --> rotation --> relative coordinates
    rotated = []
    for i in range(len(arr[0])):
        tmp = []
        for j in range(len(arr)):
            tmp.append(0)
        rotated.append(tmp)
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            rotated[j][len(arr)-i-1] = arr[i][j]
            
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
    
def set_block(board, y, x, cover_type, delta):
    ok = True
    
    for i in range(block_num):
        new_x = x + rotations[cover_type][i][1]
        new_y = y + rotations[cover_type][i][0]
        
        if new_y < 0  or new_y >= H or new_x < 0 or new_x >= W:
            ok = False
        else:
            board[new_y][new_x] += delta
            if board[new_y][new_x] > 1:
                ok = False
    return ok
        

def search(place_num):
    global best, white_num
    #  가장 윗칸 반복 재귀
    # heuristic pruning
    import numpy as np
    
    print(np.array(game), white_num)
    
    if best >= white_num / block_num:
        return
    
    x, y = -1, -1
    for i in range(H):
        for j in range(W):
            if game[i][j] == 0:
                x = j
                y = i
        if y != -1:
            break
    if y == -1:
        best = max(best, place_num)
        return
    
    ret = 0
    for t in range(4):
        if set_block(game, y, x, t, 1) == True:
            white_num -= block_num
            search(place_num+1)
            white_num += block_num
        set_block(game, y, x, t, -1)
    
    # 해당 y, x칸에 무조건 블럭이 놓여야 하는 것이 아니기 때문.
    game[y][x] = 1
    search(place_num)
    game[y][x] = 0
    return ret
      
rl = input
#rl = lambda: sys.stdin.readline()

C = int(rl())

for _ in range(C):
    H,W,R,C = map(int, rl().split())
    game = []
    block = []
    white_num = 0
    for __ in range(H):
        game_row = rl()
        game_tmp = []
        for a in game_row:
            if a == '#':
                game_tmp.append(1)
            else:
                game_tmp.append(0)
                white_num += 1
        game.append(game_tmp)
    best = 0
    block_num = 0
    for ___ in range(R):
        block_row = rl()
        block_tmp = []
        for b in block_row:
            if b == '#':
                block_tmp.append(1)
                block_num += 1
            else:
                block_tmp.append(0)
        block.append(block_tmp)
    
    white_fnum = white_num
    rotations = [[], [], [], []]
    generate(block)
    search(0)
    print(best)
    
    
