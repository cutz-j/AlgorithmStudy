import sys

#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())
P = list(map(int, rl().split()))

P.sort()
present_sum, res = 0, 0
for p in P:
    present_sum += p
    res+= present_sum
    
print(res)