import sys

def rotate(x, d, k):
    for i, c in enumerate(circle):
        # x의 배수
        if (i+1) % x == 0:
            # 시계
            tmp = []
            if d == 0:
                # k칸 이전부터 -k+M까지
                for j in range(-k, -k+M):
                    tmp.append(c[j])
            # 반시계
            if d == 1:
                # k-1칸에서 거꾸로 -k-1까지
                for j in range(k, k+M):
                    if j >= M:
                        j -= M
                    tmp.append(c[j])
            # 저장
            circle[i] = tmp

def search(circle):
    delete = False
    circle_copy = [[c for c in cir] for cir in circle]
    for i in range(N):
        for j in range(-1, M):
            if 0 <= j+1 < M:
                # horizontal conv 1칸 더 봐야함 (-1, 0)
                # print(i, j, circle[i][j], circle[i][j+1])
                if circle[i][j] == circle[i][j+1] and circle[i][j] != 0 and circle[i][j+1] != 0:
                    delete = True
                    circle_copy[i][j] = 0
                    circle_copy[i][j+1] = 0
            if 0 <= i+1 < N and 0 <= j:
                # vertical conv
                if circle[i][j] == circle[i+1][j] and circle[i][j] != 0 and circle[i+1][j] != 0:
                    delete = True
                    circle_copy[i][j] = 0
                    circle_copy[i+1][j] = 0

    # no deleted, avg
    if delete == False:
        avg, num_list = 0, []
        for i in range(N):
            for j in range(M):
                if circle[i][j] != 0:
                    avg += circle[i][j]
                    num_list.append((i, j))
        avg /= len(num_list) if len(num_list) else 1
        for i, j in num_list:
            if circle[i][j] > avg:
                circle_copy[i][j] -= 1
            elif circle[i][j] < avg:
                circle_copy[i][j] += 1
    return circle_copy

rl = lambda: sys.stdin.readline()

N, M, T = map(int, rl().split())
circle = []
for _ in range(N):
    circle.append(list(map(int, rl().split())))


for _ in range(T):
    x, d, k = map(int, rl().split())
    rotate(x, d, k)
    # print()
    # print("rotate")
    # for c in circle:
    #     print(c)
    # print()
    circle = search(circle)
    # print("search")
    # for c in circle:
    #     print(c)
    # print()

res = 0
for c in circle:
    res += sum(c)
print(res)