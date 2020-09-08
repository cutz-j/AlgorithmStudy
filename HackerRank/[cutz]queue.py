from collections import deque
import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT

rl = lambda: sys.stdin.readline()

q = int(rl())
queue = deque()
for _ in range(q):
    query = rl()
    if int(query[0]) == 1:
        query, x = map(int, query.split())
        queue.append(x)
    
    elif int(query) == 2:
        queue.popleft()
    
    elif int(query) == 3:
        print(queue[0])

        
    