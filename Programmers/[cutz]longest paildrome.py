def solution(s):
    # brute-force
    answer = 0

    for i in range(len(s)):
        for j in range(len(s), i, -1):
            search = s[i:j]
            if search == search[::-1] and search:
                answer = max(len(search), answer)

    return answer