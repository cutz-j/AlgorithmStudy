from itertools import combinations


def solution(number, k):
    answer = ''
    # comb = combinations(range(0,len(number)), len(number)-k)
    # for c in comb:
    #     ans = ''
    #     for idx in c:
    #         ans += number[idx]
    #     if int(ans) > answer:
    #         answer = int(ans)
    # answer = str(answer)

    # Sliding
    idx = -1
    for j in range(len(number) - k):
        max_num = '0'
        for i in range(idx + 1, k + j + 1):
            if max_num < number[i]:
                idx = i
                max_num = number[i]
                if max_num == '9':
                    break
        answer += max_num
    return answer