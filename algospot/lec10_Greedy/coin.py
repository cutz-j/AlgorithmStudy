import sys

#rl = lambda: sys.stdin.readline()
rl = input

N, K = map(int, rl().split())
value = []
for _ in range(N):
    value.append(int(rl()))

coin_num, value_sum = 0, 0
value.sort(reverse=True)

for v in value:
    dummy = K // v
    laugh = K % v
    if dummy == 0:
        continue
    elif dummy > 1:
        coin_num += dummy
        K -= v*dummy
    else:
        if laugh == 0:
            coin_num += dummy
            break
        else:
            coin_num += dummy
            K = laugh
            
print(coin_num)