# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:22:49 2019

@author: user
"""

#input
num_case = int(input())
pattern = input()
word = [input() for _ in range(num_case)]

def wildcard(pattern,word):
    pat_len = len(pattern)
    wo_len = len(word)
    cache = [[-1 for _ in range(wo_len +1)] for _ in range(pat_len + 1)]
    
    def match(nth_p, nth_w):
        if cache[nth_p][nth_w] != -1:
            return cache[nth_p][nth_w]
        
        if nth_p < pat_len and nth_w < wo_len and (pattern[nth_p] == '?' or pattern[nth_p] == word[nth_w]):
            cache[nth_p][nth_w] = match(nth_p + 1, nth_w + 1)
            return cache[nth_p][nth_w]
        
        if nth_p == pat_len:
            return nth_w == wo_len
        
        if pattern[nth_p] == '*':
            if match(nth_p+1,nth_w) or (nth_w < wo_len and match(nth_p,nth_w+1)):
                cache[nth_p][nth_w] = True
                return True
        
        cache[nth_p][nth_w] = False
        return False
    
    return match(0,0)


#output
for w in word:
    if (wildcard(pattern,w) == True):
        print(w)
    else:
        pass