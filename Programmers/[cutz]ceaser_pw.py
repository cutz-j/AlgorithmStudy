def solution(s: str, n: int) -> str:
    answer = ''
    for cha in s:
        asc_cha = ord(cha)
        if 97 <= asc_cha <= 122:
            if asc_cha + n > 122:
                answer += chr(asc_cha+n-122+97-1)
            else:
                answer += chr(asc_cha+n)
        elif 65 <= asc_cha <= 90:
            if asc_cha + n > 90:
                answer += chr(asc_cha+n-90+65-1)
            else:
                answer += chr(asc_cha+n)
        else:
            answer += ' '
    return answer