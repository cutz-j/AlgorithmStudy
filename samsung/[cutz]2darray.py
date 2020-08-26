import sys
from collections import Counter


def new_arr(arr):
    count = Counter(arr)
    prev = 1
    res, same = [], []
    for value, length in count.most_common()[::-1]:
        same.append((value, length))
        if prev != length:
            for v, l in same:
                res.append(v)
                res.append(l)
            prev = length
            same = []
    if same:
        for v, l in same:
            res.append(v)
            res.append(l)
    return res, len(res)
    

def op(arr, direction):
    res = []
    if direction == 'row':
        max_length = 0
        for i in range(len(arr)):
            res_row, length = new_arr(arr[i])
            res.append(res_row)
            if length > max_length:
                length = max_length
        
        for i in range(len(arr)):
            row_length = len(arr[i])
            for _ in range(length - row_length):
                res[i].append(0)
        
        return res

    if direction == 'col':
        pass
        
    return


rl = input
# rl = lambda: sys.stdin.readline()

A = []
r, c, k = map(int, rl().split())

for _ in range(3):
    A.append(list(map(int, rl().split())))
    
