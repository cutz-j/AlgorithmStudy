from collections import defaultdict


def solution(participant: list, completion: list) -> str:
    answer = ''
    comp_dict = defaultdict(int)
    for com in completion:
        comp_dict[com] += 1

    for part in participant:
        comp_dict[part] -= 1
        if comp_dict[part] < 0:
            return part