import sys


rl = input
#rl = lambda: sys.stdin.readline()

N = int(rl())


five = (N // 5)+1
answer = sys.maxsize

for i in range(five):
    rest = N - ((i)*5)
    if rest % 3 == 0:
        tmp = i + (rest//3)
        if tmp < answer:
            answer = tmp

if five == 0:
    if rest % 3 != 0:
        answer = -1
    
if answer == sys.maxsize:
    answer = -1
    
print(int(answer))
 