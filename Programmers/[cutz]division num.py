def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)

    if len(answer) == 0:
        answer = [-1]
    else:
        answer.sort()
    return answer
