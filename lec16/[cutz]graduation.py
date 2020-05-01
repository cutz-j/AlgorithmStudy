import sys

INF = sys.maxsize
MAXN = 12

def bit_count(n):
    # 켜진 비트의 수 반환
    return bin(n).count("1")

def graduate(semester, taken):
    # basis --> min / max result recursive
    if cache.get((semester, taken), -1) != -1:
        return cache[(semester, taken)]
    
    if bit_count(taken) >= K:
        cache[(semester, taken)] = 0
        return cache[(semester, taken)]
    
    if semester == M:
        cache[(semester, taken)] = INF
        return cache[(semester, taken)]
    
    
    
    can_take = C[semester] & ~taken # this semester possible classes
    
    for i in range(N):
        # 수강 가능 과목이지만 선수과목 수강하지 않았을 시
        if (can_take & (1 << i)) and ((taken & R[i]) != R[i]):
            can_take &= ~(1 << i) # 해당 자리수 비트 끄기
    
    # cantake 모든 부분집합 순회
    for i in range(can_take, 0, -1):
        take = i & can_take
        if take != i:
            continue
        # 학기 수강과목을 초과한 경우
        if bit_count(take) > L:
            continue
        
        cache[(semester, taken)] = min(cache.get((semester, taken), INF), graduate(semester+1, taken | take) + 1) # why 1? --> semester가 증가하면서 절대치도 증가하여함
        # can_take: 수강가능과목 / taken: 지금까지 수강한 과목  / take: 현재 수강하려는 과목
    
    cache[(semester, taken)] = min(cache.get((semester, taken), INF), graduate(semester+1, taken))
    return cache[(semester, taken)]
    

#rl = input
rl = lambda: sys.stdin.readline()
C = int(rl())
for _ in range(C):
    cache = {}
    N, K, M, L = map(int, rl().split()) # 전공 / 수강필수 / 학기 수 / 최대 수강과목
    R, C = [], [] # 선수과목 / 개설과목
    # bitmask
    for __ in range(N):
        tmp_list = list(map(int, rl().split()))
        tmp_list.pop(0)
        tmp_bit = 0
        for i in tmp_list:
            tmp_bit |= 1 << i
        R.append(tmp_bit)
    for ___ in range(M):
        tmp_list = list(map(int, rl().split()))
        tmp_list.pop(0)
        tmp_bit = 0
        for j in tmp_list:
            tmp_bit |= 1 << j
        C.append(tmp_bit)
        
    result = graduate(0, 0)
    if result >= INF:
        print("IMPOSSIBLE")
    else:
        print(result)