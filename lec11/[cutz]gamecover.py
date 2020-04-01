import sys
import pandas as pd

cover = [[[0, 0], [1, 0], [0, 1]],
         [[0, 0], [0, 1], [1, 1]],
         [[0, 0], [1, 0], [1, 1]],
         [[0, 0], [1, 0], [1, -1]]]

def set_block(board, y, x, cover_type, delta):
    # delta 1 --> cover // -1 --> clear
    ok = True
    
    for i in range(3):
        new_x = x + cover[cover_type][i][1]
        new_y = y + cover[cover_type][i][0]
        
        # 게임판을 넘어가는 경우
        if new_y < 0 or new_y >= H or new_x < 0 or new_x >= W:
            ok = False
        # 중복으로 덮은 경우
        else:
            board[new_y][new_x] += delta
            if board[new_y][new_x] > 1: 
                ok = False
    return ok

def cover_block(board):
    x, y = -1, -1
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                x = j
                y = i
                break
        if y != -1:
            break
    # basis    
    if y == -1:
        return 1
    ret = 0
    # 4가지 방법 모두 실행
    for t in range(4):
        # block 넣기
        if set_block(board, y, x, t, 1) == True:
            ret += cover_block(board)
            # block 치우기
        set_block(board, y, x, t, -1)
    return ret
            
    
    


rl = lambda: sys.stdin.readline()
#rl = input
C = int(rl())

for _ in range(C):
    H, W = map(int, rl().split())
    block_list = []
    white, black = 0, 0
    for __ in range(H):
        block_row = rl()
        tmp_list = []
        for b in block_row:
            if b == '#':
                black += 1
                tmp_list.append(1)
            else:
                white += 1
                tmp_list.append(0)
        block_list.append(tmp_list)
        
    if white % 3 != 0:
        answer = 0
        print(answer)
        continue
    
    print(cover_block(block_list))
    
