def solution(n, results):
    win, lose = {}, {}
    for i in range(1, n + 1):
        win[i], lose[i] = set(), set()

    for i in range(1, n + 1):
        for battle in results:
            if battle[0] == i:
                win[i].add(battle[1])
            if battle[1] == i:
                lose[i].add(battle[0])

        # i에게 이긴 winner는 i에게 진 loser들을 모두 이긴다.
        for winner in lose[i]:
            win[winner].update(win[i])
        # i에게 진 loser는 i에게 이긴 winner들에게 모두 진다.
        for loser in win[i]:
            lose[loser].update(lose[i])

    answer = 0
    for i in range(1, n + 1):
        # win/lose의 합이 n-1일 경우 순위 확정
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer