import sys

def sushi():
    cache[0] = 0
    result = 0
    for budget in range(1, int(m+1)):
        candidate = 0
        for dish in range(n):
            if budget >= price[dish]:
                candidate = max(candidate, cache.get((budget-price[dish])%201, 0) + prefer[dish])
        cache[budget%201] = candidate
        result = max(result, candidate)
    return result


rl = lambda : sys.stdin.readline()
#rl = input
C = int(rl())
for _ in range(C):
    cache = {}
    price, prefer = [], []
    n, m = map(int, rl().split())
    m /= 100
    for i in range(n):
        p, pf = map(int, rl().split())
        price.append(p/100)
        prefer.append(pf)

    print(sushi())