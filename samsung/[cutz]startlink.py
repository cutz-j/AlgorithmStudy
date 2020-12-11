import sys

def dfs(start_r, link_r, start_n, link_n, n, start_t, link_t):
    global res
    if start_n == link_n == 0:
        r = abs(start_r-link_r)
        if r < res:
            res = r

    if start_n:
        for i in start_t:
            start_r += S[i][n]
            start_r += S[n][i]

        start_t.append(n)
        dfs(start_r, link_r, start_n-1, link_n, n+1, start_t, link_t)
        for i in start_t:
            start_r -= S[i][n]
            start_r -= S[n][i]
        start_t.remove(n)


    if link_n:
        for i in link_t:
            link_r += S[i][n]
            link_r += S[n][i]
        link_t.append(n)
        dfs(start_r, link_r, start_n, link_n-1, n+1, start_t, link_t)
        for i in link_t:
            link_r -= S[i][n]
            link_r -= S[n][i]
        link_t.remove(n)


rl = lambda: sys.stdin.readline()

N = int(rl())
S = []
for _ in range(N):
    S.append(list(map(int, rl().split())))
res = sys.maxsize
dfs(0, 0, N//2, N//2, 0, [], [])
print(res)