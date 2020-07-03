import sys

def move(start, to):
    print(start, to)
    
def hanoi(n, start, to, via):
    if n == 1:
        move(start, to)
        
    else:
        hanoi(n-1, start, via, to)
        move(start, to)
        hanoi(n-1, via, to, start)
    
    


#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())
cnt = 0
for n in range(N): # n번에서 2번씩 재귀돌면서 +1씩
    cnt = cnt * 2
    cnt += 1
    
print(cnt)
hanoi(N, 1, 3, 2)
