answer = 0

def dfs(v: int, idx: int, numbers: list, target: int) -> None:
    global answer
    # basis
    if len(numbers) == idx and v == target:
        answer += 1
        return
    if len(numbers) == idx:
        return

    dfs(v + numbers[idx], idx + 1, numbers, target)
    dfs(v - numbers[idx], idx + 1, numbers, target)


def solution(numbers: list, target: int) -> int:
    # a= {n >= 0}
    # numbers: given numbers
    # length --> >= 20
    # target: target number
    dfs(0, 0, numbers, target)
    return answer