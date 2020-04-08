import sys


def search(food, edible, chosen):
    # recursive exhastive search
    global best
    if chosen >= best:
        return
    
    if food == m:
        if edible.count(0) == 0:
            best = chosen
        return best
        
        
    search(food+1, edible, chosen)
    
    for j in range(len(food_list[food])):
        edible[food_list[food][j]] += 1
    search(food+1, edible, chosen+1)

    for j in range(len(food_list[food])):
        edible[food_list[food][j]] -= 1
    


rl = input
# rl = labmda: sys.stdin.readline()

C = int(rl())
for _ in range(C):
    n, m = map(int, rl().split())
    friend_list = rl().split(' ')
    food_list = []
    best = sys.maxsize
    edible = [0 for _ in range(n)]
    for __ in range(m):
        tmp = rl().split(' ')
        tmp_list = []
        for i in range(int(tmp[0])):
            tmp_list.append(friend_list.index(tmp[i+1]))    
        food_list.append(tmp_list)
    search(0, edible, 0)
    print(best)
