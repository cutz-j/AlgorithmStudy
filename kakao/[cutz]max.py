from itertools import permutations

def solution(expression):
    answer = 0
    
    operator = ['*', '+', '-']
    num_list = []
    op_list = []
    for i in expression:
        num = ''
        if i in operator:
            op_list.append(i)
            num_list.append(int(num))
            num = ''
        else:
            num += i
            
    stack = []
    operator = set(op_list)
    prior = permutations(operator)
    
        
    
    
    return answer