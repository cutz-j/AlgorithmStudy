def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        for i, w in enumerate(word):
            if i % 2 == 0:
                answer += w.upper()
            else:
                answer += w.lower()
        answer += ' '
    return answer[:-1]