import sys

rl = lambda: sys.stdin.readline()

def rotate(q, direction):
    cu = cube[q][:]
    if direction == '+':
        up_row = cu[0][:]
        down_row = cu[2][:]
        left_col = [cu[i][0] for i in range(2, -1, -1)]
        right_col = [cu[i][2] for i in range(2, -1, -1)]
        for i in range(3):
            cu[i][2] = up_row[i]
        for i in range(3):
            cu[i][0] = down_row[i]
        cu[0] = left_col
        cu[2] = right_col

    elif direction == '-':
        up_row = cu[0][:][::-1]
        down_row = cu[2][:][::-1]
        left_col = [cu[i][0] for i in range(3)]
        right_col = [cu[i][2] for i in range(3)]
        for i in range(3):
            cu[i][0] = up_row[i]
        for i in range(3):
            cu[i][2] = down_row[i]
        cu[0] = right_col
        cu[2] = left_col
    cube[q] = cu
    return cube


C = int(rl())
for _ in range(C):
    n = int(rl())
    query = rl().split()

    up = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    down = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
    left = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    right = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    front = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    back = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]

    cube = {'U':up, 'D':down, 'L':left, 'R':right, 'F':front, 'B':back}
    link = {'U':['F','R','B','L'],
            'D':['F','R','B','L'],
            'L':['U','F','D','B'],
            'R':['U','F','D','B'],
            'B':['U','L','D','R'],
            'F':['U','L','D','R']}

    for qd in query:
        q, d = qd[0], qd[1]
        if q == 'U':
            if d == '+':
                left = [cube['L'][i][2] for i in range(2, -1, -1)]
                right = [cube['R'][i][0] for i in range(2, -1, -1)]
                front = cube['F'][0][:]
                back =  cube['B'][0][:]
                for i in range(3):
                    cube['L'][i][2] = front[i]
                for i in range(3):
                    cube['R'][i][0] = back[i]
                cube['F'][0] = right
                cube['B'][0] = left
                cube = rotate(q, d)

            elif d == '-':
                left = [cube['L'][i][2] for i in range(3)]
                right = [cube['R'][i][0] for i in range(3)]
                front = cube['F'][0][:][::-1]
                back = cube['B'][0][:][::-1]
                for i in range(3):
                    cube['L'][i][2] = back[i]
                for i in range(3):
                    cube['R'][i][0] = front[i]
                cube['F'][0] = left
                cube['B'][0] = right
                cube = rotate(q, d)

        if q == 'D':
            if d == '+':
                left = [cube['L'][i][0] for i in range(2, -1, -1)]
                right = [cube['R'][i][2] for i in range(2, -1, -1)]
                front = cube['F'][0][:]
                back = cube['B'][0][:]
                for i in range(3):
                    cube['L'][i][0] = front[i]
                for i in range(3):
                    cube['R'][i][2] = back[i]
                cube['F'][2] = right
                cube['B'][2] = left
                cube = rotate(q, d)

            elif d == '-':
                left = [cube['L'][i][0] for i in range(3)]
                right = [cube['R'][i][2] for i in range(3)]
                front = cube['F'][2][:][::-1]
                back = cube['B'][2][:][::-1]
                for i in range(3):
                    cube['L'][i][0] = back[i]
                for i in range(3):
                    cube['R'][i][2] = front[i]
                cube['F'][2] = left
                cube['B'][2] = right
                cube = rotate(q, d)

        if q == 'L':
            if d == '+':
                up = [cube['U'][i][0] for i in range(3)]
                down = [cube['D'][i][0] for i in range(3)]
                front = [cube['F'][i][0] for i in range(2, -1, -1)]
                back = [cube['B'][i][0] for i in range(2, -1, -1)]
                for i in range(3):
                    cube['U'][i][0] = back[i]
                for i in range(3):
                    cube['F'][i][0] = up[i]
                for i in range(3):
                    cube['D'][i][0] = front[i]
                for i in range(3):
                    cube['B'][i][0] = down[i]
                cube = rotate(q, d)

            if d == '-':
                up = [cube['U'][i][0] for i in range(2, -1, -1)]
                down = [cube['D'][i][0] for i in range(2, -1, -1)]
                front = [cube['F'][i][0] for i in range(3)]
                back = [cube['B'][i][0] for i in range(3)]
                for i in range(3):
                    cube['U'][i][0] = front[i]
                for i in range(3):
                    cube['F'][i][0] = down[i]
                for i in range(3):
                    cube['D'][i][0] = back[i]
                for i in range(3):
                    cube['B'][i][0] = up[i]
                cube = rotate(q, d)

        if q == 'R':
            if d == '+':
                up = [cube['U'][i][2] for i in range(2, -1, -1)]
                down = [cube['D'][i][2] for i in range(2, -1, -1)]
                front = [cube['F'][i][2] for i in range(3)]
                back = [cube['B'][i][2] for i in range(3)]
                for i in range(3):
                    cube['U'][i][2] = front[i]
                for i in range(3):
                    cube['F'][i][2] = down[i]
                for i in range(3):
                    cube['D'][i][2] = back[i]
                for i in range(3):
                    cube['B'][i][2] = up[i]
                cube = rotate(q, d)

            if d == '-':
                up = [cube['U'][i][2] for i in range(3)]
                down = [cube['D'][i][2] for i in range(3)]
                front = [cube['F'][i][2] for i in range(2, -1, -1)]
                back = [cube['B'][i][2] for i in range(2, -1, -1)]
                for i in range(3):
                    cube['U'][i][2] = back[i]
                for i in range(3):
                    cube['F'][i][2] = up[i]
                for i in range(3):
                    cube['D'][i][2] = front[i]
                for i in range(3):
                    cube['B'][i][2] = down[i]
                cube = rotate(q, d)

        if q == 'F':
            if d == '+':
                prev = cube[link[q][::-1][-1]][2] # U의 front 방면
                # R D L U
                for l in link[q][::-1]:
                    prev_r = cube[l][2]
                    cube[l][2] = prev
                    prev = prev_r[:]
                cube = rotate(q, d)

            if d == '-':
                prev = cube[link[q][-1]][2]
                for l in link[q]:
                    prev_r = cube[l][2]
                    cube[l][2] = prev
                    prev = prev_r[:]
                cube = rotate(q, d)

        if q == 'B':
            if d == '-':
                prev = cube[link[q][::-1][-1]][0]
                for l in link[q][::-1]:
                    prev_r = cube[l][0]
                    cube[l][0] = prev
                    prev = prev_r[:]
                cube = rotate(q, d)

            if d == '+':
                prev = cube[link[q][-1]][0]
                for l in link[q]:
                    prev_r = cube[l][0]
                    cube[l][0] = prev
                    prev = prev_r[:]
                cube = rotate(q, d)

    for u in cube['U']:
        print(''.join(u))