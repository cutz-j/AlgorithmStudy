# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:13:22 2019

@author: samle
"""

from functools import lru_cache
MOD = 1000000007 

@lru_cache()
def tiling(width):
    if width <= 1:
        return 1
    else:
        return((tiling(width-2)+tiling(width-1))% MOD)

def asym(width):
    if (width % 2 == 1):
        return((tiling(width) - tiling(width/2) + MOD) % 2)
    else:
        ret = tiling(width)
        ret = ((ret - tiling(width/2) + MOD) % MOD)
        ret = ((ret - tiling(width/2 - 1) + MOD) % MOD)
        return ret
        
if __name__ =='__main__':
    width = int(input())
    print()
    print('number of ways to lay tiles with width of ',width,' =  ',asym(width))