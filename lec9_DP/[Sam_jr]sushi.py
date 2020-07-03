# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:57:22 2020

@author: samle
"""

def solve():
    cache[0] = 0
    ret = 0
    for m in range(1,budget):
        cand = 0
        for dish in range(num_sushi):
            if(budget >=Sprice[dish]):
                cand = max(cand,cache.get[(budget-Sprice[dish])%201]+pref[dish])
        cache[budget%201]=cand
        ret=max(ret,cand)
    return ret
if __name__=='__main__':
    test_case = int(input())
    num_sushi,budget = [int(x) for x in input().split()]
    for _ in range(test_case):
        items = []
        cache={}
        prefer=[]
        Sprice=[]
        for _ in range(num_sushi):
            price, pref = input().split()
            price = int(price)
            Sprice.append(price/100)
            pref = int(pref)
            prefer.append(pref)
            print(solve())
        