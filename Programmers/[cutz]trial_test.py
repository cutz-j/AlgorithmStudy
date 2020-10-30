def solution(answers):
    answer = [0, 0, 0]
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    for i, ans in enumerate(answers):
        if one[i] == ans:
            answer[0] += 1
        if two[i] == ans:
            answer[1] += 1
        if three[i] == ans:
            answer[2] += 1

    answer_copy = sorted(answer[:], reverse=True)
    res = []
    for i, ans in enumerate(answer):
        if answer_copy[0] == ans:
            res.append(i + 1)
    return res