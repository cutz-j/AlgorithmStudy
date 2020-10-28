from itertools import permutations
import sys

sys.setrecursionlimit(100000)


def prime(n: int) -> bool:
    # search prime number
    if n != 1:
        for f in range(2, n):
            if n % f == 0:
                return False
    else:
        return False
    return True


def solution(numbers):
    # numbers length <= 7
    # numbers number 0~9
    answer = 0
    result = []
    res_set = set()
    for i in range(1, len(numbers) + 1):
        comb = permutations(numbers, i)
        for c in comb:
            num = int(''.join(c))
            if num in res_set or num == 0:
                continue
            res_set.add(num)
            if prime(num):
                answer += 1
    return answer