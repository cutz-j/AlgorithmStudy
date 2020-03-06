# time over
import sys

volume_list = []
need_list = []
name_list = []
n = -1 # item length wanted
cache = [] # dp
picked = []

def pack(capacity, i):

    # basis
    if cache[capacity][i] != -1:
        return cache[capacity][i]
    if i >= len(name_list) or capacity <= 0:
        return 0
    # not pick up
    result = pack(capacity, i+1)
    if volume_list[i] <= capacity:
        result = max(result, need_list[i] + pack(capacity-volume_list[i], i+1))
    cache[capacity][i] = result
    return result

def reconstruct(capacity, i):
    # basis
    if i >= len(name_list):
        return

    if pack(capacity, i) == pack(capacity, i+1):
        reconstruct(capacity, i+1)
    else:
        picked.append(name_list[i])
        reconstruct(capacity-volume_list[i], i+1)

    

#rl = lambda : sys.stdin.readline()
rl = input
for _ in range(int(rl())):
    n, w = map(int, rl().split())
    cache = [[-1]*(n+1) for _ in range(w+1)]
        
    for i_ in range(n):
        item, volume, need = rl().split()
        
        name_list.append(item)
        volume_list.append(int(volume))
        need_list.append(int(need))
    
    picked = []
    reconstruct(w, 0)
    print(cache[w][0], len(picked))
    for item_ in picked:
        print(item_)