import sys

def find_possible(start):
    start_val = house[start]
    visited[start] = True
    if n == start+1:
        return start
    
    while True:
        if start+2 <= n:
            next_val = house[start+1]
            if next_val - start_val > k:
                break
            else:
                start += 1
                visited[start] = True
        else:
            break   
    return start


def visit(start):
    start_val = house[start]
    while True:
        if start+2 <= n:
            next_val = house[start+1]
            if next_val - start_val > k:
                break
            else:
                start += 1
                visited[start] = True
        else:
            break
    return start+1
            
        



rl = input
#rl = lambda: sys.stdin.readline()

n, k = map(float, rl().split())
n = int(n)
house = list(map(int, rl().split()))
house = sorted(house)

visited = [False for i in range(n)]

start, cnt = 0, 0
while True:
    start = visit(find_possible(start))
    cnt += 1
    if start == n:
        break


print(cnt)

