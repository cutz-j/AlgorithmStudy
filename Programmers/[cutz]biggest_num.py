# https://programmers.co.kr/learn/courses/30/lessons/42746
import functools


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)  # 3 --> 3자리가 max (1,000 까지)
    return str(int(''.join(numbers)))


def comp(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution_2(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comp), reverse=True)
    return str(int(''.joint(n)))