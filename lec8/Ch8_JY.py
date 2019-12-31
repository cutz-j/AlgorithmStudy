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









# O(2자승) 풀이
from itertools import product
count = int(input())


for _ in range(count):
    _ = input()
    num_list = input().split(" ")
    num_list = [int(x) for x in num_list]
    global_counter=0
    cheat = list(product([0,1],repeat=len(num_list)))
   
    for elem in cheat:
        temp = [a*b for a,b in zip(elem,num_list)]
        temp = [i for i in temp if i != 0]
        if global_counter > len(temp):
            pass
        else:
            if sorted(set(temp))==temp:
                if global_counter<len(temp):
                    global_counter=len(temp)
                
    print(global_counter)
    
        
# 더 빠른 풀이 jis
def lis(lr):
    vector =[]
    for part in lr:
        if not vector:
            vector.append(part)
        else:
            if vector[-1]<part:
                vector.append(part)
                # print(vector)
            elif vector[-1]> part:
                for index,element in enumerate(vector):
                    if element> part:
                        vector[index]=part
                        break
    return vector
                    
                
   
    
    
count = int(input())


for _ in range(count):
    _ = input()
    num_list = input().split(" ")
    num_list = [int(x) for x in num_list]
    print(len(lis(num_list)))


# jlis

def jlis(lr,lr1):
    indexer_1=0
    indexer_2=0
    vector=0
    while indexer_1 < len(lr) or indexer_2 < len(lr1):
    
    if not vector:
        vector.append(lr[indexer_1])
        indexer_1+=1
    else:
        if indexer_1 < len(lr):
            if vector[-1]< lr[indexer_1]:
                vector.append(lr[indexer_1])
                indexer_1+=1
            elif vector[-1]> lr[indexer_1]:
                for index,element in enumerate(vector):
                    if element> lr[indexer_1]:
                        vector.insert(index,lr[indexer_1])
                        break
                indexer_1+=1
            elif vector[-1]== lr[indexer_1]:
                indexer_1+=1
        elif indexer_2 < len(lr1):
            if vector[-1]< lr1[indexer_2]:
                vector.append(lr1[indexer_2])
                indexer_2+=1
            
            elif vector[-1]> lr1[indexer_2]:
                for index,element in enumerate(vector):
                    if element> lr1[indexer_2]:
                        vector.insert(index,lr1[indexer_2])
                        break
                indexer_2+=1
            elif vector[-1] == lr1[indexer_2]:
                indexer_2+=1
            else:
                pass
    return vector




count = int(input())


for _ in range(count):
    _ = input()
    num_list = input().split(" ")
    num_list1 = input().split(" ")
    num_list = [int(x) for x in num_list]
    num_list1 = [int(x) for x in num_list1]
    print(len(set(jlis(num_list,num_list1))))

# poliomino

def poly(n,first):
    if n==first:
        return 1
    if CACHE[n][first] != -1:
        return CACHE[n][first]
    ret =0
    for second in range(1,n-first+1):
        ret += (second +first -1)*poly(n-first,second)
        ret = ret%MOD
    CACHE[n][first] =ret
    return ret



count = int(input())
MOD = 10*1000*1000
CACHE = [[-1 for j in range(101)] for k in range(101)]


for _ in range(count):
    answer = 0
    number = int(input())

    for index in range(1,number+1):
        answer += poly(number,index)
        answer = answer%10000000
    print(answer)