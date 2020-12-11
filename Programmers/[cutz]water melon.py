def solution(n):
    answer = ''
    if n // 2:
        answer += '수박' * (n // 2)
    if n % 2:
        answer += '수'

    return answer