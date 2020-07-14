import sys


#rl = lambda: sys.stdin.readline()
rl = input

money = int(rl())
coin = [500, 100, 50, 10, 5, 1]
change = 1000 - money
count = 0
for c in coin:
    if change == 0:
        break
    div = change // c
    if div == 0:
        continue
    else:
        change -= (c * div)
        count += div
        
print(count)