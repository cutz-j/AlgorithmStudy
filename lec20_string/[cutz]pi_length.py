import sys
from itertools import combinations

def get_pi(N):
    m = len(N)
    pi = [0]*m
    
    begin, matched = 1, 0
    while begin + matched < m:
        if N[begin+matched] == N[matched]:
            matched += 1
            pi[begin+matched-1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
    return pi

string = str(input()) 
strings = [] 
for i in range(len(string)): 
    for j in range(len(string) - i): 
        strings.append(string[j:j+i+1]) 

print(len(set(strings)))
