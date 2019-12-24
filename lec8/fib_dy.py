# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:35:00 2019

@author: user
"""


from functools import lru_cache

#@lru_cache()
#Explicit Method
cache = {}
def fibo1(n):
    if n in cache:
        return cache[n]
    elif n <= 2:
        value = 1
    else:
        value = fibo1(n-1) + fibo1(n-2)
        
        cache[n] = value
        
    return value


if __name__ =='__main__':
    for i in range(10001):
        print(i,':',fibo1(i))

#implicit method
@lru_cache(maxsize=10000)
def fibo2(n):
    if n < 2:
        return 1
    else:
        return(fibo2(n-1)+fibo2(n-2))
        
if __name__ =='__main__': 
    for i in range(10001):
        print(i,':',fibo2(i))
