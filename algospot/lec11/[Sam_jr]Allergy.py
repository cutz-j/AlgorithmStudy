# -*- coding: utf-8 -*-
import sys

def search(edible,chosen):
    global best
    if chosen >= best:
        return
    
    first = 0
    
    while((first < num_friends) & (edible[first]>0)):
        first += 1
    
    if first == num_friends:
        best = chosen
        return 
    
    for i in range(len(canEat[first])):
        food = canEat[first][i]
        for j in range(len(eaters[food])):
            edible[eaters[food][j]] += 1
        search(edible,chosen+1)
        for j in range(len(eaters[food])):
            edible[eaters[food][j]] -= 1
        

if __name__=='__main__':
    
    test_case = int(input())

    for _ in range(test_case):
        best = sys.maxsize
        num_friends, food_num = [int(x) for x in input().split()]
        friends_lst=[x for x in input().split()]
        #friends_lst.append([[x for x in input().split()]])
            
        tmp = []
        edible = [0 for _ in range(num_friends)]
        
        for _ in range(food_num):
            tmp.append([x for x in input().split()])
            
        eaters = [ce[1:] for ce in tmp]
        
        canEat = []
        
        canEat = []
        for fl in friends_lst:
            canEat.append([i for i ,v in enumerate(tmp) if fl in v])
        search(edible,0)
        print(best)
    
    