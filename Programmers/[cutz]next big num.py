def solution(n):
    answer = 0
    c_one = bin(n).count('1')
    for i in range(n+1, 1000001):
        if bin(i).count('1') == c_one:
            return i