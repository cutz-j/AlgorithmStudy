import sys
from collections import Counter


def new_arr(arr):
    count = Counter(arr)
    res, same = [], []
    sorted_count = count.most_common()[::-1]
    prev = sorted_count[0][1] if sorted_count[0][0] != 0 else sorted_count[1][1]
     
    for value, length in sorted_count:
        if value == 0:
            continue
        if prev != length:
            for v, l in sorted(same):
                res.append(v)
                res.append(l)
            same = []
            same.append((value, length))
        else:
            same.append((value, length))
        prev = length
        
    if same:
        for v, l in sorted(same):
            res.append(v)
            res.append(l)
    return res, len(res)
    

def op(arr, direction, row_len, col_len):
    res, res_tmp, length_list = [], [], []
    if direction == 'row':
        max_length = 0
        for i in range(row_len):
            res_row, length = new_arr(arr[i])
            res.append(res_row)
            length_list.append(length)
            if length > max_length:
                max_length = length
        
        if max_length > 100:
            max_length = 100
        
        for i in range(row_len):
            row_length = length_list[i]
            if row_length > 100:
                for j in range(1, row_length-100+1):
                    res.pop(-j)
            
            for _ in range(max_length - row_length):
                res[i].append(0)
        
        return res

    if direction == 'col':
        max_length = 0
        for i in range(col_len):
            t_arr = []
            for j in range(row_len):
                t_arr.append(arr[j][i])
            res_col, length = new_arr(t_arr)
            res_tmp.append(res_col)
            length_list.append(length)
            if length > max_length:
                max_length = length
        
        if max_length > 100:
            max_length = 100
            
        res = [[0]*col_len for _ in range(max_length)]
        for i, r in enumerate(res_tmp):
            for j, v in enumerate(r):
                if j > 100:
                    break
                res[j][i] = v 
        return res


rl = input
# rl = lambda: sys.stdin.readline()

A = []
r, c, k = map(int, rl().split())

for _ in range(3):
    A.append(list(map(int, rl().split())))

cnt = 0
while True:
    if cnt > 100:
        print(-1)
        break
    
    try:
        if A[r-1][c-1] == k:
            print(cnt)
            break
    
    except:
        pass
    
    row_len, col_len = len(A), len(A[0])
    
    if row_len >= col_len:
        A = op(A, 'row', row_len, col_len)
    else:
        A = op(A, 'col', row_len, col_len)
    
    cnt += 1
    
    
    
    
    
    
    
    
    
    
    
