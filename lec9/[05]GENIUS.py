def get_prb(K, wanted, song_length, T):
    N = len(song_length)
    cache = [[0 for _ in range(N)] for _ in range(5)]
    cache[0][0] = 1.0
    probs = [0 for _ in range(N)]
    ret = []

    for time in range(1, K+1):
        for nxt in range(N):
            tmp = 0
            for prev in range(N):
                tmp += cache[(time-song_length[prev]+5) % 5][prev] * T[prev][nxt]
            cache[time % 5][nxt] = tmp

    for song in range(N):
        for start in range(K-song_length[song]+1, K+1):
            probs[song] += cache[start % 5][song]

    for m in wanted:
        ret.append(probs[m])

    return ret


C = int(input())
ans = []

for _ in range(C):
    N, K, M = [int(n) for n in input().split()]
    T = [None for _ in range(N)]
    song_length = [int(n) for n in input().split()]
    for i in range(N):
        T[i] = [float(n) for n in input().split()]

    wanted = [int(n) for n in input().split()]
    ans.append(get_prb(K, wanted, song_length, T))

for n in ans:
    print(' '.join(str(c) for c in n))
