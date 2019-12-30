# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 01:33:44 2019

@author: user
"""
import time

def ites(target,number):
    num_seq = [1983]
    for num in range(1,number):
        num_seq.append(((num_seq[num-1]*214013 + 2531011) % (2**32)))

    for num in range(1,number):
        num_seq[num] = num_seq[num] % 10000 + 1

    q = []
    count = 0
    for num in num_seq:
        if (num == target) | (sum(q) == target): # c1
            count += 1
            del q[::]
        #print('c1:',q)
        
        elif sum(q) < target:#c2
            q.append(num)
        
        #print('c2:',q)
        else: #c3
            q.append(num)
            while sum(q) > target:
                q.pop(0)
                
                
    return count        
        
if __name__ == '__main__':
    t1 = time.time()
    test_case = int(input())
    abc = [input().split() for _ in range(test_case)]
    for a in abc:
        print(ites(int(a[0]),int(a[1])))
    t2 = time.time()
    print(t2-t1)
 