def countA(name):
    idx = [0, 0]
    a_cnt, max_a = 0, 0
    diff = []
    Z = 26
    for i, c in enumerate(name):
        if c == 'A':
            diff.append(0)
            a_cnt += 1
        else:
            d = ord(c) - ord('A')
            diff.append(d if d < Z/2 else Z - d)
            if a_cnt > max_a: max_a, idx = a_cnt, [i-a_cnt, i]
            a_cnt = 0
    return (diff, a_cnt, [len(name)-a_cnt, len(name)]) if a_cnt > max_a else (diff, max_a, idx)

def solution(name):
    answer = 0
    diff, max_A, idx = countA(name)
    if max_A == 0:
        return sum(diff) + len(name) - 1
    if max_A == len(name):
        return 0
    if idx[1] == len(name):
        return sum(diff) + idx[0] - 1
    if idx[0] == 0:
        return sum(diff) + len(name) - idx[1]
    if max_A >= idx[0]:
        if idx[0] <= len(name) - idx[1]:
            return sum(diff) + (idx[0] - 1) * 2 + len(name) - idx[1]
        else:
            return sum(diff) + idx[0] - 1 + (len(name) - idx[1]) * 2
    else:
        return sum(diff) + len(name) - 1