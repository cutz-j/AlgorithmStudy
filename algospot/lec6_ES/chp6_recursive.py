# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:39:53 2019

@author: user
"""

def recursiveSum(n):
    if n == 1:
        return 1
    else:
        return n + recursiveSum(n-1)

if __name__ =='__main__':
    print(recursiveSum(3))
    print(recursiveSum(10))