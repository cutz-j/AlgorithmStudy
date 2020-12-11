def solution(people: list, limit: int) -> int:
    # greedy
    # sort --> insert --> count
    # minimize 가방의 남은 공간
    answer = 0
    people.sort() # nlgn
    i,j = 0, len(people)-1
    while i <= j:
        answer += 1
        if people[j]+people[i] <= limit:
            i += 1
        j -= 1
    return answer