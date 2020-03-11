import sys

empty = -987654321
dp_dict = {}

def play(numbers):
    # basis
    length = len(numbers)
    case1 = empty
    case2 = empty
    if length == 0:
        return 0

    if dp_dict.get((tuple(numbers)), -1) != -1:
        return dp_dict[(tuple(numbers))]
    
    if length >= 2:
        case1 = -play(numbers[2:])
        case2 = -play(numbers[:-2])
    
    case3 = numbers[0] - play(numbers[1:])
    case4 = numbers[-1] - play(numbers[:-1])
    
    ret = max(case1, case2, case3, case4)
    dp_dict[tuple(numbers)] = ret
    return ret

rl = lambda : sys.stdin.readline()
#rl = input
C = int(rl())
for _ in range(C):
    n = int(rl())
    board = list(map(int, rl().split()))
    
    print(play(board))
    
    