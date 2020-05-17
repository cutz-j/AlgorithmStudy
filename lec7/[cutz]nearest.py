import sys
from itertools import combinations


answer = sys.maxsize

def distance(dot1, dot2):
    return (dot2[0]-dot1[0])**2 + (dot2[1]- dot1[1])**2

## combination memory over
#def nearest(possible):
#    global answer
#    
#    for p in possible:
#        tmp = distance(p)
#        if tmp < answer:
#            answer = tmp
#
## time over
#def nearest_recursive(idx):
#    global answer
#    if idx == N:
#        return
#    
#    for i in range(idx+1, N):
#        tmp = distance((dot_list[idx], dot_list[i]))
#        if tmp < answer:
#            answer = tmp
#        nearest_recursive(i)
#
## excpet case 
#def nearest_sorted():
#    global answer
#    for i in range(N-1):
#        tmp = (sum_list[i]-sum_list[i+1])**2
#        answer = min(tmp, answer)
#    
# divide&conqure
def nearest_dc(start, end):
    # start - end 사이에 존재하는 가장 거리가 가까운 두 점 거리 제곱
    diff = end - start
    # basis
    if diff == 1:
        return 0
    elif diff == 2:
        return distance(dot_list[start], dot_list[start+1])
    elif diff == 3:
        a = distance(dot_list[start], dot_list[start+1])
        b = distance(dot_list[start], dot_list[start+2])
        c = distance(dot_list[start+1], dot_list[start+2])
        return min(a, min(b, c))
    
    # divide
    mid_idx = (start+end) // 2
    mid_y = dot_list[mid_idx][0]
    
    partition_one = nearest_dc(start, mid_idx)
    partition_two = nearest_dc(mid_idx, end)
    
    min_partition_value = min(partition_one, partition_two)
    part_list = []
    
    for i in range(start, end):
        if (mid_y - dot_list[i][0])**2 <= min_partition_value:
            part_list.append(dot_list[i])
            
    # x sort
    part_list.sort(key=lambda value: value[1])
    length_part = len(part_list)
    
    if length_part >= 2:
        for i in range(length_part-1):
            for j in range(i+1, length_part):
                # 초과
                if (part_list[j][1] - part_list[i][1])**2 > min_partition_value:
                    break
                # 같은 part
                elif part_list[j][0] < mid_y and part_list[i][0] < mid_y:
                    continue
                elif part_list[j][0] > mid_y:
                    continue
                dist = distance(part_list[j], part_list[i])
                if dist < min_partition_value:
                    min_partition_value = dist
    part_list = []
    return min_partition_value



    

#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())
dot_list, sum_list = [], []
for _ in range(N):
    y, x = map(int, rl().split(' '))
    dot_list.append([y, x])
dot_length = len(dot_list)
dot_set = list(set(map(tuple, dot_list)))
set_length = len(dot_set)

dot_set.sort()

if dot_length != set_length:
    print(0)
else:
    print(nearest_dc(0, len(dot_set)))
