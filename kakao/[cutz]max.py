from itertools import permutations

def prior_op(a, b, priority):
    op_a = priority[a]
    op_b = priority[b]
    
    if op_a > op_b:
        return 1
    elif op_a < op_b:
        return -1
    else:
        return 0

def solution(expression):
    answer = 0
    operator = ['*', '+', '-']
    all_list = []
    op_list = []
    num = ''
    for i in expression:
        if i in operator:
            all_list.append(num)
            all_list.append(i)
            op_list.append(i)
            num = ''
        else:
            num += i
    if num:
        all_list.append(num)
    operator = set(op_list)
    prior = permutations(operator)    
    answer_list = []
    for p in prior:
        priority = {p_op:idx for idx, p_op in enumerate(p)}
        stack = []
        order = []
        
        for i in range(len(all_list)):
            tok = all_list[i]
            if tok.isdigit():
                order.append(tok)
            else:
                while len(stack) != 0 and prior_op(stack[-1], all_list[i], priority) >= 0:
                    order.append(stack.pop(-1))
                stack.append(tok)
        
        while len(stack) != 0:
            order.append(stack.pop(-1))
        
        
        stack = []
        for i in range(len(all_list)):
            tok = order[i]
            if tok.isdigit():
                stack.append(int(tok))
            else:
                op2 = stack.pop(-1)
                op1 = stack.pop(-1)
                
                if tok == '+':
                    stack.append(op1 + op2)
                elif tok == '*':
                    stack.append(op1 * op2)
                else:
                    stack.append(op1 - op2)
                    
        answer_list.append(abs(stack.pop(-1)))
        
    answer = max(answer_list)
    return answer