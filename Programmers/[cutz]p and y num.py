def solution(s):
    answer = True
    s = s.lower()
    p_num, y_num = 0, 0
    for c in s:
        if c == 'p':
            p_num += 1
        if c == 'y':
            y_num += 1

    if p_num == y_num:
        return True
    else:
        return False
