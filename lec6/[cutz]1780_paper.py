import sys

def paper(size, y, x):
    global minus_num, zero_num, one_num
    minus, zero, one = True, True, True
    if size == 1:
        if mat[y][x] == -1:
            minus_num += 1
        elif mat[y][x] == 0:
            zero_num += 1
        else:
            one_num += 1
        return
    
    for i in range(y, y+size):
        for j in range(x, x+size):
            if mat[i][j] == -1:
                zero, one = False, False
            elif mat[i][j] == 0:
                minus, one = False, False
            else:
                minus, zero = False, False
    if minus:
        minus_num += 1
    elif zero:
        zero_num += 1
    elif one:
        one_num += 1
    else:
        new_size = int(size/3)
        paper(new_size, y, x)
        paper(new_size, y, x+new_size)
        paper(new_size, y, x+(new_size*2))
        paper(new_size, y+new_size, x)
        paper(new_size, y+new_size, x+new_size)
        paper(new_size, y+new_size, x+(new_size*2))
        paper(new_size, y+(new_size*2), x)
        paper(new_size, y+(new_size*2), x+new_size)
        paper(new_size, y+(new_size*2), x+(new_size*2))
    return


#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())
minus_num, zero_num, one_num = 0, 0, 0
mat = []
for i in range(N):
    mat.append(list(map(int, rl().split(' '))))

paper(N, 0, 0)
print(minus_num)
print(zero_num)
print(one_num)