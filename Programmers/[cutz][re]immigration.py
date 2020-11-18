import heapq

def impossible(n, middle, times):
    return sum([middle // x for x in times]) < n

def solution(n, times):
    # 입국 심사
    # 각 심사대
    # n: length of waiting
    # times: time cost
    answer = 0
    left, right = 1, max(times)*n
    while left < right:
        mid = (left + right) // 2
        if impossible(n, mid, times):
            left = mid + 1
        else:
            right = mid
    return left