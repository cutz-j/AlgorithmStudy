import sys


def possible(K, M):
    m = 1
    k = K
    cum = 0
    for need in expense:
        need += cum
        if need <= k:
            k -= need
        elif need > k:
            m += 1
            k = K
            if need <= k:
                k -= need
            else:
                cum += need
    if m > M or cum > 0:
        return False
    else:
        return True


# rl = lambda: sys.stdin.readline()
rl = input

N, M = map(int, rl().split())
expense = []
for _ in range(N):
    expense.append(int(rl()))
    

minimum = max(expense)
if possible(minimum, M):
    print(minimum)
else:
    left, right = minimum, 1e9
    while left != right:
        mid = int((left + right)/2)
        if possible(mid, M):
            right = mid
        else:
            left = mid+1
    print(left)