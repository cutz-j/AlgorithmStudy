from collections import defaultdict
from itertools import product


def solution(clothes):
    answer = 1
    hash_dict = defaultdict(int)
    for c, category in clothes:
        hash_dict[category] += 1

    for key in hash_dict:
        answer *= (hash_dict[key] + 1)

    answer -= 1
    return answer