import sys
from queue import PriorityQueue



rl = lambda: sys.stdin.readline()
#rl = input
C = int(rl())

for _ in range(C):
    n = int(rl())
    length = list(map(int, rl().split()))
    
    pq = PriorityQueue()
    
    for i in length:
        pq.put(i)
    
    ret = 0
    
    while len(pq.queue) > 1:
        min1 = pq.get()
        min2 = pq.get()
        
        pq.put(min1+min2)
        ret += min1 + min2
    
    print(ret)