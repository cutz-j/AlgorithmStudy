import sys

def food(idx, sour=1, bitter=0):
    global ret
    
    if idx > N:
        return
    
    # 누적을 적용
    sour *= item[idx][0]
    bitter += item[idx][1]
    diff = abs(sour - bitter)
    ret = min(ret, diff)
    for i in range(idx+1, N):
        food(i, sour, bitter)


#rl = lambda: sys.stdin.readline()
rl = input
ret = sys.maxsize
cache = {}
N = int(rl())
item = []
for _ in range(N):
    item.append(list(map(int, rl().split())))
    
for i in range(N):
    food(i)

print(ret)