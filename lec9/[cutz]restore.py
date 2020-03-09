import sys
sys.setrecursionlimit(10000)

MAX = 15
cache = [[-1]*((1<<MAX)+1+1) for _ in range(MAX+1)]

def pp(k_list):
    for i in range(len(k_list)):
        removed = False
        for j in range(len(k_list)):
            if i != j and k_list[i] in k_list[j]:
                k_list.pop(i)
                removed = True
                break
        if removed == True:
            continue
    
    return k_list

def overlap(k_i, k_j):
    length = min(len(k_i), len(k_j))
    for l in range(length, 0, -1):
        if k_i[len(k_i)-l:] == k_j[:l]:
            return l
    return 0

def restore(last, now):
    # 완전탐색
    # basis
    if now == (1<<K)-1:
        return 0
   
    # memoization
    result = cache[last][now]
    if result != -1:
        return result # dp
    
    result = 0
    
    for k in range(K):
        if (last & (1 << k)) == 0:
            candidate = overlap_list[last][k] + restore(k, now+(1<<k))
            result = max(result, candidate)
    
    cache[last][now] = result
    return result
    

# complete search
# 순서에 따라서 모든 경우의 수 generate
# we need only length of the generated sentences
# length(i) + length(j) - overlap(i, j)
# maximize overlap(i, j)
    

#rl = lambda : sys.stdin.readline()
rl = input
C = int(rl())
for _ in range(C):
    K = int(rl())
    k_list = []
    for __ in range(K):
        k_list.append(rl())
    
    k_list = pp(k_list)
    K = len(k_list)
    overlap_list = [[-1]*(K) for __ in range(K)]
    # 미리 overlap 저장 (K^2)
    for i in range(K):
        for j in range(K):
            if i == j:
                continue
            else:
                overlap_list[i][j] = overlap(k_list[i], k_list[j])

    

