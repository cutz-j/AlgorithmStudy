# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:12:14 2020

@author: user
"""


# -*- coding: utf-8 -*-

def LunchBox(NumLunch,Heating_T,Eating_T):
    eating = {}
    for idx, eat in enumerate(Eating_T):
        eating[idx] = eat
        
    eating_priority = sorted(eating.items(),key = lambda itm:itm[1],reverse=True)
    
    result, pri = 0,0
    for n in range(NumLunch):
        box = eating_priority[n][0]
        pri += Heating_T[box]
        
        result = max(result,pri + Eating_T[box])
    
    return result

if __name__ =='__main__':   
    tc = int(input())
    for t in range(tc):
        num_lunch = int(input())
        heating_time = list(map(int,input().split()))
        eating_time = list(map(int,input().split()))
    
        print(LunchBox(num_lunch,heating_time,eating_time))