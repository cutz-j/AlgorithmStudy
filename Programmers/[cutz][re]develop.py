import math


class Queue:
    def __init__(self):
        self.front, self.rear = 0, 0
        self.list = []
        self.pop_count = 0

    def append(self, x):
        self.list.append(x)
        self.rear += 1

    def pop(self):
        res = self.list[self.front]
        self.front += 1
        self.pop_count += 1
        return res

    def empty(self):
        return len(self.list) == self.pop_count


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