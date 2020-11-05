from collections import defaultdict


def solution(n: int, lost: list, reserve: list) -> int:
    # n = student num
    # lost: lost num
    # reserve: who can give clothes
    answer = 0
    # reserve_dict
    res = defaultdict(int)
    length = len(lost)
    same = 0
    for r in reserve:
        if r not in lost:
            res[r] += 1
        else:
            same += 1
            del lost[lost.index(r)]

    answer = n - length + same
    for l in lost:
        print(l, res, answer)
        if res[l - 1]:
            answer += 1
            res[l - 1] -= 1
        elif res[l + 1]:
            answer += 1
            res[l + 1] -= 1
    return answer