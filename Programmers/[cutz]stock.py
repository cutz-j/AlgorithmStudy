# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top

        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top

    return answer