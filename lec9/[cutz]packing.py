# time over
import sys

volume_list, need_list, name_list = [], [], []
n = -1 # item length wanted
cache = [[]] # dp
picked = []

def pack(capacity, i):
    '''
    function: calculate mximum needs in the capacity
    input:
        - capacity
        - i
    output:
        - maximum needs
    '''
    # basis
    if i == n:
        return 0
    ret = cache[capacity][i]
    if ret != -1:
        return ret
    # not pick up
    ret = pack(capacity, i+1)
    
    # pick up
    if capacity >= volume_list[i]:
        ret = max(ret, pack(capacity - volume_list[i], i+1) + need_list[i])
    cache[capacity][i] = ret
    return ret

def reconstruct(capacity, i):
    '''
    function:
        
    '''
    # basis
    if i == n:
        return
    # present item != next item --> present maximum list
    present_n = pack(capacity, i)
    next_n = pack(capacity, i+1)
    if present_n == next_n:
        reconstruct(capacity, i+1)
    else:
        picked.append(name_list[i])
        reconstruct(capacity - volume_list[i], i+1)

    

rl = lambda : sys.stdin.readline()
#rl = input
for _ in range(int(rl())):
    n, w = map(int, rl().split())
    cache = [[-1] * (n + 1) for _ in range(w + 1)]
        
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