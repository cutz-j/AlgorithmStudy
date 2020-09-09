#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
import copy


# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    strr = list(s)
    palin = list(s)
    
    l = 0
    r = n - 1
    
    while l <= r:
        # replace maximum
        if strr[l] != strr[r]:
            palin[l] = palin[r] = max(strr[l], strr[r])
            k -= 1
        
        l += 1
        r -= 1
    
    if k < 0:
        return '-1'
    
    l = 0
    r = n - 1
    
    while l <= r:
        # mid: 1개로 변경 가능
        if l == r:
            if k > 0:
                palin[l] = '9'
                
        if palin[l] < '9':
            # none chanced before --> k -= 1
            if k >= 2 and palin[l] == strr[l] and palin[r] == strr[r]:
                k -= 2
                palin[l] = palin[r] = '9'
            # one changed before --> k -= 1
            elif k >= 1 and (palin[l] != strr[l] or palin[r] != strr[r]):
                k -= 1
                palin[l] = palin[r] = '9'
        
        l += 1
        r -= 1
    
    return ''.join(palin)


'''
def num_palindrome(s,n, k):
    cnt = 0
    l = 0
    r = n-1
    while l <= r:
        if s[l] != s[r]:
            cnt += 1
        l += 1
        r -= 1
    return cnt

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    if k >= n:
        return '9'*n

    cnt = num_palindrome(s, n, k)
    print(cnt)
    if cnt > k:
        return '-1'

    k_comb = combinations(range(n), k)
    answer = '0'
    for c in k_comb:
        s_copy = list(s)
        for i in c:
            s_copy[i] = 'k'
        
        if s_copy[0] != 'k':
            if int(s_copy[0]) < int(answer[0]):
                continue
        elif s_copy[0] == 'k' and s_copy[-1] != 'k':
            if int(s_copy[-1]) < int(answer[0]):
                continue   

        stop = False
        l, r = 0, n-1
        while l <= r:

            if s_copy[l] == 'k' and s_copy[r] == 'k':
                s_copy[l], s_copy[r] = '9', '9'
            
            elif s_copy[l] == 'k' and s_copy[r] != 'k':
                s_copy[l] = s_copy[r]
            
            elif s_copy[l] != 'k' and s_copy[r] == 'k':
                s_copy[r] = s_copy[l]

            elif s_copy[l] != s_copy[r]:
                stop = True
                break

            l += 1
            r -= 1
        
        if not stop:
            pal = int(''.join(s_copy))
            if pal > int(answer):
                answer = str(pal)

    if answer == '0':
        answer = '-1'
    return answer
'''

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()
    
    result = highestValuePalindrome(s, n, k)

#    fptr.write(str(result) + '\n')
#
#    fptr.close()
