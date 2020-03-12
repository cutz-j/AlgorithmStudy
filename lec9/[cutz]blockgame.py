import sys

move = []

def cell(y, x):
    return 1 << (y*5 + x)

def precalc():
    
    for y in range(4):
        for x in range(4):
            cells = []
            
            for dy in range(2):
                for dx in range(2):
                    cells.append(cell(y+dy, x+dx))
            
            square = cells[0] + cells[1] + cells[2] + cells[3]
            for i in range(4):
                move.append(square - cells[i])
            
    for i in range(5):
        for j in range(4):
            move.append(cell(i, j) + cell(i, j+1))
            move.append(cell(j, i) + cell(j+1, i))
            
def play(board):
    if cache.get(board, -1) != -1:
        return cache[board]
    ret = 0
    for i in range(len(move)):
        if move[i] & board == 0:
            if play(board | move[i]) == 0:
                ret = 1
                break
    cache[board] = ret
    return ret


#rl = lambda : sys.stdin.readline()
rl = input
C = int(rl())
precalc()
for _ in range(C):
    board = 0
    cache = {}
    for i in range(5):
        row = rl()
        for j in range(5):
            if row[j] == '#':
                board += cell(i, j)
    result = play(board)
    print('WINNING') if result else print("LOSSING")

