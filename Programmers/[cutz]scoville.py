import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    prev = 0
    for s in scoville:
        heapq.heappush(heap, s)

    while len(heap) >= 2:
        first = heapq.heappop(heap)
        if first >= K:
            break
        if heapq:
            second = heapq.heappop(heap)
        else:
            answer = -1
            break
        new = first + (second * 2)
        heapq.heappush(heap, new)
        answer += 1
    if heap[0] < K:
        answer = -1
    return answer