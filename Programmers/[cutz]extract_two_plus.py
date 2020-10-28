from itertools import combinations

def solution(numbers: list) -> list:
    answer = []
    comb = combinations(numbers, 2)
    for i,j in comb:
        answer.append(i+j)
    answer = sorted(list(set(answer)))
    return answer