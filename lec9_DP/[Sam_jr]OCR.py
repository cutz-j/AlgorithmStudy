# -*- coding: utf-8 -*-



m,q = [int(x) for x in input().split()]
w = input().split()
B = [float(x) for x in input().split()]
M = []
T = []
test = []
cache = [[[1]*102]*502]
choice = [[[-1]*102]*502]
R = [[-1]*100]
n = -1
corpus = [[-1]*501]


def recognize(segment,prev_match):
    if segment == n:
        return 0
    
    ret = cache[segment][prev_match]
    
    if (ret != 1.0):
        return ret
    ret = float('-inf')
    
    choose = choice[segment][prev_match]
    

    for t in range(m):
        cand = T[prev_match][t] + M[t][R[segment]] + recognize(segment+1,t)
        
        if ret < cand:
            ret = cand
            choose = t
    
    return ret

def reconstruct(segment,prev_match):
    choose = choice[segment][prev_match]
    ret = corpus[choose]
    
    if (segment < n-1):
        ret = ret + " "+reconstruct(segment+1,choose)
    return ret

if __name__ =='__main__':
    for _ in range(m):
        tmp = [float(x) for x in input().split()]
        T.append(tmp)

    for _ in range(m):
        tmp = [float(x) for x in input().split()]
        M.append(tmp)

    for _ in range(q):
        test.append(input().split())
    
    for t in test:
        t[0] = int(t[0]) 
    
    recognize(0,0)
    print(reconstruct(0,0))
    