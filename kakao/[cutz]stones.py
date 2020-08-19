import sys

'''
def solution_range_sum(stones, k):
    # 구간합은 최적해를 보장하지 않
    answer = 0
    if len(stones) == 1:
        answer += len(stones)
        return answer
    range_sum = {idx: sum(stones[idx:idx+k]) for idx in range(len(stones)-k)}
    min_idx = min(range_sum.keys(), key=(lambda k: range_sum[k]))
    while True:
        for idx in range(min_idx, min_idx+k):
            stones[idx] -= 1
        answer += 1
        if sum(stones[min_idx:min_idx+k]) == 0:
            break
    answer += 1
    return answer음
'''

def init(stones, N):
    t = 1
    tree = [-sys.maxsize]*(4*N)
    while t <= N:
        t *= 2
    
    for i in range(N):
        tree[t+i] = stones[i]
    
    for i in range(t-1, 0, -1):
        tree[i] = max(tree[i*2], tree[i*2+1])
    
    return tree

def query_max(l, r, N, tree):
    t = 1
    while t <= N:
        t *= 2
    tl = t + l
    tr = t + r
    s = 0
    while tl <= tr:
        if tl % 2 == 1:
            if tree[tl] > s:
                s = tree[tl]
            tl += 1
        elif tr % 2 == 0:
            if tree[tr] > s:  
                s = tree[tr]
            tr -= 1
        tl //= 2
        tr //= 2
    return s


def solution(stones, k):
    answer = sys.maxsize
    N = len(stones)
    if N == 1:
        return stones[0]
    if N == k:
        return max(stones)
    if k == 1:
        return min(stones)
    tree = init(stones, N)
    for i in range(N-k+1):
        range_max = query_max(i, i+k-1, N, tree)
        if range_max < answer:
            answer = range_max
    return answer
    