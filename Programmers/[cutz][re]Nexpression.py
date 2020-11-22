# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    # 각 dp 사용횟수에서 달성할 수 있는 최소 최적화
    answer = -1
    dp = []
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            for x in dp[j]:
                for y in dp[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    if y != 0:
                        numbers.add(x // y)
        if number in numbers:
            answer = i
            break

        dp.append(numbers)

    # answer = min(cache.values())
    return answer