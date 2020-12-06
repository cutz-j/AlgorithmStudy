def solution(s):
    if len(s) == 4 or len(s) == 6:
        for cha in s:
            if ord(cha) < 48 or ord(cha) > 57:
                return False
        return True
    else:
        return False