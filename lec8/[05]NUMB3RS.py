import sys
input = sys.stdin.readline


# Bottom-up
def prob_in_there(base, target, days):
    cache = [[-1 for _ in range(len(adj_matrix))] for _ in range(days+1)]

    # find(d, here): d일 후 here에 있을 때, 최종 days일 때 target에 있을 확률
    def find(passed, here):
        if days == passed:
            return 1 if here == target else 0
        elif cache[passed][here] != -1:
            return cache[passed][here]

        ret = 0
        for there in range(len(cache[0])):
            if adj_matrix[there][here]:
                ret += find(passed+1, there)
        ret /= degrees[here]
        cache[passed][here] = ret
        return ret

    return find(0, base)


# Top-down
def prob_in_there(base, target, days):

    # find(d, here): d일 째에 here에 있을 확률
    def find(here, time):
        if time == 0:
            return 1 if here == base else 0
        elif cache[time][here] != -1:
            return cache[time][here]
        else:
            ret = 0
            for there in range(len(adj_matrix)):
                if adj_matrix[there][here]:
                    ret += find(there, time-1) / degrees[there]
            cache[time][here] = ret
            return ret
    return find(target, days)


C = int(input())
ans = []

for _ in range(C):
    N, D, start = (int(n) for n in input().split())
    adj_matrix = []
    degrees = []
    cache = [[-1 for _ in range(N)] for _ in range(D+1)]

    for _ in range(N):
        line = [int(x) for x in input().split()]
        adj_matrix.append(line)
        degrees.append(sum(line))

    input()
    targets = [int(x) for x in input().split()]
    ret = []
    for t in targets:
        ret.append(str(prob_in_there(start, t, D)))

    ans.append(' '.join(ret))

for n in ans:
    print(n)
