import sys
from collections import deque
from itertools import combinations
import copy

def change_number(n, i, j):
    tmp_i, tmp_j = n[i], n[j]
    n[i], n[j] = tmp_j, tmp_i
    return n

#def exchange(n, i, j, k):
#    if len(str(n)) != length:
#        return -1
#    if k == K+1:
#        return n
#    if cache.get((n, i, j), -1) != -1:
#        return cache[(n, i, j)]
#    
#    new_num = change_number(n, i, j)
#    for idx in range(length-1):
#        for jdx in range(idx+1, length):
#            cache[(n, i, j)] = max(cache.get((n, i, j), -1), exchange(new_num, idx, jdx, k+1))
#    return cache[(n, i, j)]

def bfs():
    visited = set()
    q_length = len(q)
    answer = 0
    while q_length:
        x = q.popleft()
        present_n = list(str(x))
        for i, j in comb_list: # 모든 조합 try
            tmp_n = copy.deepcopy(present_n)
            changed_n = change_number(tmp_n, i, j)
            if changed_n[0] == '0':
                continue
            new_n = int(''.join(changed_n))
            if new_n not in visited:
                answer = max(answer, new_n)
                visited.add(new_n)
                q.append(new_n)
        q_length -= 1
    return answer


#rl = lambda: sys.stdin.readline()
rl = input

N, K = map(int, rl().split())
length = len(str(N))
item_list = [i for i in range(length)]
comb_list = list(combinations(item_list, 2))
q = deque()
q.append(N)
while K:
    answer = bfs()
    K -= 1
if not answer:
    print(-1)
else:
    print(answer)