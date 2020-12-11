def solution(brown: int, yellow: int) -> list:
    # brown: 테두리, 8 ~ 5*10**3
    # yellow: center, 1 ~ 2*10**6
    answer = []

    for h in range(1, yellow + 1):
        w, l = divmod(yellow, h)
        if w < h:
            break
        if l != 0:
            continue
        ans_w, ans_h = w + 2, h + 2
        brown_num = (ans_w * 2) + (ans_h - 2) * 2
        if brown_num == brown:
            answer.append(ans_w)
            answer.append(ans_h)
            return answer