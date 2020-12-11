def solution(n: int) -> list:
    if n % 2 == 0:
        # even
        all_length_idx = (1 + n) * (n // 2)
    else:
        # odd
        all_length_idx = (1 + n) * (n // 2) + (n // 2) + 1
    ans = 1
    answer = [-1] * all_length_idx
    # first left
    idx, i, prev_list = 0, 1, []
    while idx < all_length_idx:
        prev_list.append(idx)
        answer[idx] = ans
        idx += i
        i += 1
        ans += 1
    # 0: left-down, 1: left-right, 2: right-up
    direction, jump_num = 1, 1
    # length --> n, n-1, n-2, ..., 1
    for i in range(n - 1, 0, -1):
        p_list = []
        if direction == 0:
            for j in range(len(prev_list) - 1, len(prev_list) - i - 1, -1):
                idx = prev_list[j] + jump_num
                p_list.append(idx)
                answer[idx] = ans
                ans += 1
            jump_num += 1
        elif direction == 1:
            idx = prev_list[-1]
            for k in range(idx + 1, idx + i + 1):
                answer[k] = ans
                ans += 1

        else:
            for j in range(len(prev_list) - 1, len(prev_list) - i - 1, -1):
                idx = prev_list[j] - jump_num
                p_list.append(idx)
                answer[idx] = ans
                ans += 1
            jump_num += 1
        direction += 1
        if direction == 3:
            direction = 0
        if p_list:
            prev_list = p_list

    return answer