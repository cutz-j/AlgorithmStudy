import sys

def dp(now, prev_idx):
    if now == n-1:
        return triangle[now][prev_idx]
    
    if cache.get((now, prev_idx), -1) != -1:
        return cache[(now, prev_idx)]
    
    dp_left = dp(now+1, prev_idx)
    dp_right = dp(now+1, prev_idx+1)
    cache[(now, prev_idx)] = triangle[now][prev_idx] + max(dp_left, dp_right)
    return cache[(now, prev_idx)]
     

#rl = lambda: sys.stdin.readline()
rl = input

n = int(rl())
triangle = []
cache = {}
for _ in range(n):
    triangle.append(list(map(int, rl().split())))
    
print(dp(0, 0))
