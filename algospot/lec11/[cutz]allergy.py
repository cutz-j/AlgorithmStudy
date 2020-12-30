import sys


def search(food, edible, chosen):
    # recursive exhastive search
    global best
    if chosen >= best:
        return
    
    # basis
    if food == m: # 모든 음식 search
        if edible.count(0) == 0: # 다 먹었다면,
            best = chosen # best
        return best
        
    # food search
    search(food+1, edible, chosen)
    
    
    for j in range(len(food_list[food])):
        edible[food_list[food][j]] += 1
    search(food+1, edible, chosen+1)

    for j in range(len(food_list[food])):
        edible[food_list[food][j]] -= 1
    
def search2(edible, chosen):
    global best
    
    if chosen >= best:
        return
    
    first = 0
    
    # 친구 기준으로 계산
    while first < n and edible[first] > 0:
        first += 1
    
    # 먹을 수 있는 음식
    if first == n:
        best = chosen
        return
    
    for i in range(len(can_list[first])):
        food = can_list[first][i]
        for j in range(len(food_list[food])):
            edible[food_list[food][j]] += 1
        search2(edible, chosen+1)
        for j in range(len(food_list[food])):
            edible[food_list[food][j]] -= 1
            
             
    

rl = input
#rl = lambda: sys.stdin.readline()

C = int(rl())
for _ in range(C):
    n, m = map(int, rl().split())
    friend_list = rl().split(' ')
    eat_list, can_list = [], []
    for i in range(n):
        can_list.append([])
    
    food_list = []
    best = sys.maxsize
    edible = [0 for _ in range(n)]
    for f in range(m):
        tmp = rl().split(' ')
        tmp_list = []
        for i in range(int(tmp[0])):
            tmp_list.append(friend_list.index(tmp[i+1]))
            can_list[friend_list.index(tmp[i+1])].append(f)
        food_list.append(tmp_list)
    search2(edible, 0)
    print(best)
