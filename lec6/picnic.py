# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:12:01 2019

@author: user
"""

import numpy as np

areFriend = np.zeros((10,10),dtype=bool)
n = 10


taken = np.zeros((1,10),dtype=bool)
def countPairings(*taken):
    firstFree = -1
    for i in range(n):
        if not taken[i]:
            firstFree = i
            break
        
    if firstFree == -1:
        ret = 0
    
    for pairWith in range(n):
        pairWith = firstFree + 1
        if ((not taken[pairWith]) and (areFriend[firstFree][pairWith])):
            taken[firstFree] = True
            taken[pairWith] = True
            ret += countPairings(*taken)
            taken[firstFree] = False
            taken[pairWith] = False
            
    return ret
        


