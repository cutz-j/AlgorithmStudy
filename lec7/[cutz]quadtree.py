import sys

def quadtree(size, y, x):
#    print("print", size, y, x)
    if size == 1:
        print(mat[y][x], end='')
        return
    
    zero, one = True, True
    for i in range(y, y+size):
        for j in range(x, x+size):
            if int(mat[i][j]) == 1:
                zero = False
            elif int(mat[i][j]) == 0:
                one = False
                
    if zero:
        print(0, end='')
    elif one:
        print(1, end='')
    else:
        print("(", end='')
        quadtree(size >> 1, y, x) # 2 사분면
        quadtree(size >> 1, y, x+(size>>1)) # 1 사분면
        quadtree(size >> 1, y+(size>>1), x) # 3 사분면
        quadtree(size >> 1, y+(size>>1), x+(size>>1)) # 4 사분면
        print(")", end='')
    return
    


#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())

mat = []
for _ in range(N):
    mat.append(rl())

quadtree(N, 0, 0)
