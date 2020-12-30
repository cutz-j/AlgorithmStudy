import sys

rl = input
# rl = lambda:sys.stdin.readline()

N = int(rl())
data = [rl().strip() for _ in range(N*2-2)]
hint = []
for i in range(2*N-2):
    length = len(data[i])
    if length == N-1:
        hint.append(data[i])
    data[i] = (length, data[i])

sp_list = []
first, second = hint[0], hint[1]
if first[1:] == second[:-1]:
    sp_list.append(first + second[-1])
if first[:-1] == second[1:]:
    sp_list.append(second + first[-1])


for sp in sp_list:
    prefix, suffix = [0]*(N-1), [0]*(N-1)
    res = ''
    for length, d in data:
        if prefix[length-1] == 0 and d == sp[:length]:
            res += 'P'
            prefix[length-1] = 1
            continue
        if suffix[length-1] == 0 and d == sp[-length:]:
            res += 'S'
            suffix[-length] = 1
            continue
    if len(res)==2*N-2:
        print(sp)
        print(res)
        break