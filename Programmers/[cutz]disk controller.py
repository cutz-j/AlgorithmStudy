# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq
from collections import deque


def solution(jobs: list) -> int:
    # disk controller
    # start, cost
    jobs.sort()
    queue = deque(jobs)
    done, time, wait, heap = 0, 0, 0, []
    while done < len(jobs):
        if not heap:
            s, t = queue.popleft()
            time = s + t
            wait += t
        else:
            t, s = heapq.heappop(heap)
            time += t
            wait += time - s

        done += 1

        while queue and queue[0][0] <= time:
            heapq.heappush(heap, queue.popleft()[::-1])

    return wait // len(jobs)