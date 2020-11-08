def solution(people: list, limit: int) -> int:
    # greedy
    # sort --> insert --> count
    # minimize 가방의 남은 공간
    answer = 1
    people.sort() # nlgn
    cum = 0
    for weight in people:
        print(cum, weight, answer)
        if limit - cum >= weight:
            cum += weight
        else:
            answer += 1
            cum = weight
    return answer