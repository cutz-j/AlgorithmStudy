# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 01:28:51 2019

@author: user
"""
from functools import lru_cache
MOD = 1000000007 

@lru_cache()
def tiling(width):
    if width <= 1:
        return 1
    else:
        return((tiling(width-2)+tiling(width-1))% MOD)

if __name__ =='__main__':
    width = int(input())
    print()
    print('number of ways to lay tiles with ',width,' width = ',tiling(width))
    