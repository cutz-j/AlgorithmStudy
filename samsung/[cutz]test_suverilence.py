import sys

rl = input
# rl = lambda: sys.stdin.readline()

N = int(rl())
A = list(map(int, rl().split()))
B, C = map(int, rl().split())


answer = 0
# 총 감독관
for i in range(N):
    A[i] -= B
    answer += 1
    if A[i] > 0:
        if A[i] % C == 0:
            answer += A[i] // C
        else:
            answer += (A[i] // C) + 1

print(answer)

    



