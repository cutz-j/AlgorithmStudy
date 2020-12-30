# -*- coding: utf-8 -*-

import heapq as hq
import sys

def med_calc(seq,a,b):
    seed = 1983
    median = 0
    min_heap = []
    max_heap = []
    
    hq.heapify(min_heap)
    hq.heapify(max_heap)

    for _ in range(seq):
        #Adding the first value 
        if (len(min_heap) == 0) and (len(max_heap)==0):
            hq.heappush(max_heap,-seed)
            median += seed
            
        #Appending values     
        elif max_heap:
            if seed >= -max_heap[0]:
                hq.heappush(min_heap,seed)
            else:
                hq.heappush(max_heap,-seed)
            # Calculating the median
            if len(max_heap) == len(min_heap):
                median += -max_heap[0]
                
            elif (len(max_heap)) == (len(min_heap)+1):
                median += -max_heap[0]
                
            elif (len(min_heap)) == (len(max_heap)+1):
                median += min_heap[0]
                
            # Rebalancing heaps    
            elif len(min_heap) == (len(max_heap) + 2):
                hq.heappush(max_heap,-hq.heappop(min_heap))
                median += -max_heap[0]
                
            elif len(max_heap) == (len(min_heap)+2):
                hq.heappush(min_heap,-hq.heappop(max_heap))
                median += -max_heap[0]
                
        seed = ((seed * a) + b) % 20090711
        
    return median % 20090711

if __name__ == '__main__':
    #print(med_calc(1273,4936,10000))
    test_case = int(input())
    for _ in range(test_case):
        a,b,c  = [int(x) for x in input().split()]
        print(med_calc(a,b,c))

