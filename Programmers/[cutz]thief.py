from collections import defaultdict

def solution(money: list) -> int:
    # CIRCLE! --> 시작과 끝이 겹칠 수 없음
    # money -> 각 집의 돈
    # length 3 <= 10**6
    # O(N) --> impossible
    # subproblem --> 이전까지의 max값 (X) [1,2,3,4,30]
    # 선택은 다다음이냐 다다다음이냐로 결정 --> block
    cache = defaultdict(int)
    cache[0] = money[0]
    cache[1] = max(money[0], money[1]) # 첫 DP max
    for i in range(2, len(money)-1):
        cache[i] = max(cache[i-1], cache[i-2]+money[i])
    answer = cache[len(money)-2]
    cache = defaultdict(int)
    cache[0] = 0
    cache[1] = money[1]
    for i in range(2, len(money)):
        cache[i] = max(cache[i-1], cache[i-2]+money[i])
    answer = max(answer, cache[len(money)-1])
    return answer