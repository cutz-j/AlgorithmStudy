import sys

def dp(now, step):
    if now == len_stair-1:
        return stair[now]
    
    


#rl = lambda: sys.stdin.readline()
rl = input

len_stair = int(rl())
stair = [int(rl()) for _ in range(len_stair)]
