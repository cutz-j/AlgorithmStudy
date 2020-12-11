def solution(a, b):
    answer = sum(range(a,b+1)) if a < b else sum(range(b,a+1))
    return answer