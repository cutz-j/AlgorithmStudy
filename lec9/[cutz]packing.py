# time over
import sys

volume_list, need_list, name_list = [], [], []
n = -1 # item length wanted
cache = [[]] # dp

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
    return ret

def reconstruct(capacity, i, picked, score):
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
        reconstruct(capacity, i+1, picked, score)
    else:
        picked.append(name_list[i])
        score.append(present_n)
        reconstruct(capacity - volume_list[i], i+1, picked, score)

    

rl = lambda : sys.stdin.readline()
#rl = input
for _ in range(int(rl())):
    n, w = map(int, rl().split())
    cache = [[-1]*(n+1)]*(w+1) # index
        
    for i_ in range(n):
        item, volume, need = rl().split()
        
        name_list.append(item)
        volume_list.append(int(volume))
        need_list.append(int(need))
    
    picked = []
    score_list = []
    reconstruct(w, 0, picked, score_list)
    print(max(score_list), len(picked))
    for item_ in picked:
        print(item_)