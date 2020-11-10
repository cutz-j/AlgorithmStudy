def solution(a: list) -> int:
    # array balloon different numbers
    # bomb, remaining only one
    # 1. choose randomly adjcent two balloon, and busrt one
    # 2. if empty space, make dense balloon
    # bursting smaller number is only once
    # return possible survived balloon number
    # length a = 10**7
    # 1) minimum
    # 2) larger value in left or right
    answer = 2
    left, right = a[0], a[-1]
    for i in range(1, len(a)-1):
        if left > a[i]:
            left = a[i]
            answer += 1
        if right > a[-i-1]:
            right = a[-i-1]
            answer += 1
    # 중복 제거
    if left == right:
        answer -= 1
    return answer