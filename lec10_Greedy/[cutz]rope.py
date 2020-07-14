import sys

rl = input
#rl = lambda: sys.stdin.readline()

N = int(rl())
weight = []
for _ in range(N):
    weight.append(int(rl()))
    
cnt = 0
max_weight = 0

weight = sorted(weight, reverse=True)

for n, w in enumerate(weight):
    max_w = w*(n+1)
    if max_weight < max_w:
        max_weight = max_w
        
print(max_weight)
