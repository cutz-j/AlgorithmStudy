import sys

def get_size(mask):
    num, compare = 0, 1
    for i in range(1, 10):
        compare = compare << 1
        if compare and mask:
            num += 1
    return num

def get_sum(mask):
    summation, compare = 0, 1
    for i in range(1, 10):
        compare = compare << 1
        if compare and mask:
            summation += i
    return summation

def get_candidate(length, summation, known):
    all_set = 0
    for i in range(0, 1024, 2):
        if (i and known) == known and get_size(i) == length and get_sum(i) == summation:
            all_set |= i
    return all_set & ~known

def generate_candidate():
    candidates = []
    for _ in range(10):
        tmp1 = []
        for __ in range(46):
            tmp2 = []
            for ___ in range(1024):
                tmp2.append(0)
            tmp1.append(tmp2)
        candidates.append(tmp1)
        
    for i in range(0, 1024, 2):
        l = get_size(i)
        s = get_sum(i)
        subset = i
        while True:
            candidates[l][s][subset] |= (i and ~subset)
            if subset == 0:
                break
            subset = (subset - 1) and i
    return candidates

#rl = lambda: sys.stdin.readline()
rl = input
C = int(rl())
candidates = generate_candidate()
for _ in range(C):
    N = int(rl())
    color, hint, value = [], [], []
    for __ in range(N):
        row = list(map(int, rl().split()))
        value_row = [0 for t in range(N)]
        hint_row = [0 for t in range(N) for t_ in range(2)]
        color.append(row)
        value.append(value_row)
        hint.append(hint_row)
            
        
    
    Q = int(rl())
    
    for ___ in range(Q):
        y, x, direction, sum_value = map(int, rl().split())
        
    
    mask = []