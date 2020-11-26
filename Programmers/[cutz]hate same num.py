def solution(arr):
    # 중복 수 제거 / 순서 유지
    # 10**6 --> O(n)
    answer = [arr[0]]
    for a in arr[1:]:
        if a == answer[-1]:
            continue
        else:
            answer.append(a)
    return answer