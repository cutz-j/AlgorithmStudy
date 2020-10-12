from collections import defaultdict
import sys

sys.setrecursionlimit(9999999)
cache = defaultdict(int)


def dp(n):
    if n <= 1:
        return 1

    if cache.get(n, None):
        return cache[n]

    cache[n] = (dp(n - 2) + dp(n - 1)) % 1000000007
    return cache[n]


def solution(n):
    answer = dp(n)
    return answer

print(solution(60000))