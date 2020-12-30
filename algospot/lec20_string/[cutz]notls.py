import sys


rl = input
# rl = lambda:sys.stdin.readline()

N, M = map(int, rl().split())

a, b = set(), set()
for _ in range(N):
    a.add(rl())

for i in range(M):
    b.add(rl())
       
word_list = list(a&b)
word_list.sort()

print(len(word_list))
for w in word_list:
    print(w)