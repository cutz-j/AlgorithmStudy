def solution(progresses, speeds):
    answer = []
    while progresses:
        for i, p in enumerate(progresses):
            progresses[i] = p + speeds[i]

        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt:
            answer.append(cnt)
    return answer