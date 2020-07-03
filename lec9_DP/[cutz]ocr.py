import sys
import math

n, m = -1, -1
R = [-1.]*100
T = [[-1.]*501]*501
M = [[-1.]*501]*501
choice = [[-1]*102]*502
cache = [[1]*102]*502

def recognize(segment, previous_match):
    if segment == n:
        return 0
    ret = cache[segment][previous_match]
    if ret != 1.0:
        return ret
    ret = -1e200
    choose = choice[segment][previous_match]
    
    for t in range(m):
        cand = math.log(T[previous_match][t]) + math.log(M[t][R[segment]]) + math.log(recognize(segment+1, t))
        
        if ret < cand:
            ret = cand
            choose = t        
    return ret

def reconstruct(corpus, segment, previous_match):
    choose = choice[segment][previous_match]
    ret = corpus[choose]
    if segment < n-1:
        ret = ret + " " + reconstruct(corpus, segment+1, choose)
    return ret



rl = input
#rl = lambda : sys.stdin.readline()

m, q = map(int, rl().split()) # m = word lenfth, q = sentences length
word = rl().split() # word
B = rl().split() # first word prob
T = [] # transition matrix
for _ in range(m):
    t = rl().split()
    t.insert(0, B[_])
    T.append(t)
M = [] # word matrix
for _ in range(m):
    mal = rl().split()
    M.append(mal)



for _ in range(q):
    length_sentence = rl().split()
    
    w = length_sentence.pop(0)
    for i in range(m):
        if length_sentence[i] == word[i]:
            R[_] = i
            
    recognize(0, 0)
    print(reconstruct(length_sentence, 0, 0))
    
    
    



    