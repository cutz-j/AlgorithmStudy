from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    weight_sum = 0
    while queue:
        time += 1
        w = queue.popleft()
        weight_sum -= w
        if truck_weights:
            if weight_sum + truck_weights[0] <= weight:
                weight_sum += truck_weights[0]
                queue.append(truck_weights.popleft())
            else:
                queue.append(0)
    return time