import sys

def dfs(r, c, d1, d2, ans):
    while True:
        while True:
            lr, lc, rr, rc = r + d1, c - d1, r + d2, c + d2  # left, right
            if rr == N-1 or rc == N:
                break
            br, bc = r + d1 + d2, c - d1 + d2 # bottom
            if br >= N or bc >= N or bc < 0:
                break
            ans = min(ans, find_min(r, c, lr, lc, rr, rc, bc))
            d2 += 1
        d1 += 1
        if r + d1 == N-1 or c - d1 == -1:
            break
        d2 = 1
    return ans

def find_min(r, c, lr, lc, rr, rc, bc):
    g1, g2, g3, g4 = 0, 0, 0, 0
    d = 0
    # 0 < left_r (row), and 0 < y+1
    for i in range(lr):
        for j in range(c+1):
            # 대각선 찾기
            if (i, j) == (r+d, c-d):
                d += 1
                break
            g1 += A[i][j]
    d = 1
    for i in range(rr+1):
        for j in range(N-1, c, -1):
            if (i, j) == (r + d, c + d):
                d += 1
                break
            g2 += A[i][j]

    d = 0
    for i in range(lr, N):
        for j in range(bc):
            if (i, j) == (lr + d, lc + d):
                d += 1
                break
            g3 += A[i][j]

    d = 1
    for i in range(rr+1, N):
        for j in range(N-1, bc-1, -1):
            if (i, j) == (rr + d, rc - d):
                d += 1
                break
            g4 += A[i][j]

    g5 = all_sum - g1 - g2 - g3 - g4
    max_v = max(g1, g2, g3, g4, g5)
    min_v = min(g1, g2, g3, g4, g5)
    return max_v - min_v


rl = lambda: sys.stdin.readline()

N = int(rl())
A, all_sum = [], 0
for _ in range(N):
    tmp = list(map(int, rl().split()))
    all_sum += sum(tmp)
    A.append(tmp)

ans = sys.maxsize
for i in range(N-2):
    for j in range(1, N-1):
        d1, d2 = 1, 1
        ans = dfs(i, j, d1, d2, ans)

print(ans)