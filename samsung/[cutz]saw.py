import sys

def rotate(index, direction):
    if index == None:
        return None

    if direction == 1:
        index -= 1
    elif direction == -1:
        index += 1

    if index < 0:
        index = 7
    elif index > 7:
        index = 0
    return index


def step(saw_num, direction, pointer_dict):
    pointer = pointer_dict[saw_num]
    change = [False, False, False]
    if saw[0][pointer_dict[1][1]] != saw[1][pointer_dict[2][0]]:
        change[0] = True
    if saw[1][pointer_dict[2][1]] != saw[2][pointer_dict[3][0]]:
        change[1] = True
    if saw[2][pointer_dict[3][1]] != saw[3][pointer_dict[4][0]]:
        change[2] = True

    new_p = []
    for p in pointer:
        if p == None:
            new_p.append(None)
            continue
        new_p.append(rotate(p, direction))
    pointer_dict[saw_num] = new_p

    before = range(saw_num-1, 0, -1)
    after = range(saw_num+1, 5)
    before_d = direction
    after_d = direction
    for i in before:
        if change[i-1]:
            before_d = -before_d
            new_p = []
            for p in pointer_dict[i]:
                if p == None:
                    new_p.append(None)
                    continue
                new_p.append(rotate(p, before_d))
            pointer_dict[i] = new_p
        else:
            break

    for i in after:
        if change[i-2]:
            after_d = -after_d
            new_p = []
            for p in pointer_dict[i]:
                if p == None:
                    new_p.append(None)
                    continue
                new_p.append(rotate(p, after_d))
            pointer_dict[i] = new_p
        else:
            break

    return pointer_dict


rl = lambda: sys.stdin.readline()

saw = []
for _ in range(4):
    saw.append(list(rl().strip()))

# init
one_two = 2
two_one = 6
two_three = 2
three_two = 6
three_four = 2
four_three = 6
pointer_dict = {1:[None, one_two], 2:[two_one, two_three], 3:[three_two, three_four], 4:[four_three, None]}

K = int(rl())
query = []
for _ in range(K):
    query.append(list(map(int, rl().split())))
for q_n, direction in query:
    pointer_dict = step(q_n, direction, pointer_dict)

answer = 0
r = rotate(pointer_dict[1][1], 1)
one_t = rotate(r, 1)
if saw[0][one_t] == '1':
    answer += 1
r = rotate(pointer_dict[2][1], 1)
two_t = rotate(r, 1)
if saw[1][two_t] == '1':
    answer += 2
r = rotate(pointer_dict[3][1], 1)
three_t = rotate(r, 1)
if saw[2][three_t] == '1':
    answer += 4
r = rotate(pointer_dict[4][0], -1)
four_t = rotate(r, -1)
if saw[3][four_t] == '1':
    answer += 8
print(answer)

