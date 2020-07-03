# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:59:03 2019

@author: user
"""
coverType = [[[0,0],[1,0],[0,1]],
             [[0,0],[0,1],[1,1]],
             [[0,0],[1,0],[1,1]],
             [[0,0],[1,0],[1,-1]]]

def check(board,y,x,type_,delta):
    ok = True
    for i in range(3):
        ny = y + coverType[type_][i][0]
        nx = x + coverType[type_][i][1]
        if (ny < 0 | ny >= len(board) | nx < 0 | nx >= len(board[0])):
            ok = False
        elif ((board[ny][nx] + delta) > 1):
            ok = False
    return ok

#board[i][j] = 1: 이미 덮힘
#board[i][j] = 0; 아직 덮이지 않은 칸
def cover(board):
    y = -1
    x = -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 0):
                y = i
                x = j
                break
        if(y != -1):
            break

#기저 사례: 모든 칸을 채웠으면 1을 반환
    if (y ==-1):
        return 1

    ret = 0

    for type_ in range(4):
        if(check(board,y,x,type_,1)):
            ret += cover(board)
            check(board,y,x,type_,-1)

    return ret
    
        
    

    



    
