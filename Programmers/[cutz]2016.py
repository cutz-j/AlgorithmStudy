def solution(a, b):
    answer = ''
    month = {0:0, 1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = {1:'FRI',2:'SAT',3:'SUN', 4:'MON',5:'TUE',6:'WED', 0:'THU'}
    d = 0
    for i in range(0, a):
        d += month[i]
    d += b
    answer = day[(d % 7)]
    return answer