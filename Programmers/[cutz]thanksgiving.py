def solution(lines):
    answer, len_lines, count = 0, 0, 1
    start, finish = [], []
    for log in lines:
        len_lines += 1
        tmp = float(log[11:13]) * 3600 + float(log[14:16]) * 60 + float(log[17:23])
        finish.append(tmp)
        start.append(round(tmp - float(log[24:-1]) + 0.001, 3))

    for i in range(len_lines):
        count = 1
        for j in range(i + 1, len_lines):
            if finish[i] + 1 > start[j]:
                count += 1
        answer = max(answer, count)
    return answer