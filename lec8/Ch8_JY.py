TEST= int(input())

def finder(location):
    global MAP
    global MEMORY
    global GLOBAL_VARIABLE
    # out of boundary
    # 이미 찾았다면 종료
    # 가고자 하는 방향이 이미 있다면
    if GLOBAL_VARIABLE:
        return -1
    elif location[0]>= N or location[1]>= N:
        pass
        return -1

    elif location[0] ==N-1 and location[1] ==N-1:
        GLOBAL_VARIABLE=1
        return -1

    elif MEMORY[location[0]][location[1]]==1 or MEMORY[location[0]][location[1]]==-5:
        return -1
    else:
        jump_size = MAP[location[0]][location[1]]
        MEMORY[location[0]][location[1]]+=1
        finder([location[0]+jump_size,location[1]])
        MEMORY[location[0]][location[1]]+=1
        finder([location[0],location[1]+jump_size])
        

for _ in range(TEST):
    N = int(input())
    MAP = []
    MEMORY = [[] for x in range(N)]
    GLOBAL_VARIABLE = 0
    # MAP preparation
    # MEMORY preparation
    # MEMORY [X][Y] = [DOWN,RIGHT]
    for index in range(N):
        temp = input()
        temp = temp.split(" ")
        temp = [int(x) for x in temp]
        MAP.append(temp)
        for _ in range(N):
            MEMORY[index].append(-1)
    finder([0,0])
    if GLOBAL_VARIABLE:
        print("YES")
    else:
        print("NO")

"""

JUMPGAME
"""
TEST= int(input())

def finder(location):
    global MEMORY
    global GLOBAL_VARIABLE
    # out of boundary
    # 이미 찾았다면 종료
    # 가고자 하는 방향이 이미 있다면
    if GLOBAL_VARIABLE:
        return -1
    elif location[0]>= N or location[1]>= N:
        return -1
    
    elif MEMORY[location[0]][location[1]]==1:
        return -1

    elif location[0] ==N-1 and location[1] ==N-1:
        GLOBAL_VARIABLE=1
        return -1
    else:
        jump_size = MAP[location[0]][location[1]]
        MEMORY[location[0]][location[1]]+=1
        finder([location[0]+jump_size,location[1]])
        MEMORY[location[0]][location[1]]+=1
        finder([location[0],location[1]+jump_size])
        

for _ in range(TEST):
    N = int(input())
    MAP = []
    MEMORY = [[] for x in range(N)]
    GLOBAL_VARIABLE = 0
    # MAP preparation
    # MEMORY preparation
    # MEMORY [X][Y] = [DOWN,RIGHT]
    for index in range(N):
        temp = input()
        temp = temp.split(" ")
        temp = [int(x) for x in temp]
        MAP.append(temp)
        for _ in range(N):
            MEMORY[index].append(-1)
    finder([0,0])
    if GLOBAL_VARIABLE:
        print("YES")
    else:
        print("NO")