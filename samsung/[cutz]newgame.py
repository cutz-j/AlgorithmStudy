import sys

def move(horse, i, r, c, nr, nc, d, second, cnt):
    link = horse[i][3]
    adj = []
    d_copy = d
    finish = False
    if 0 <= nr < N and 0 <= nc < N:
        color = chess_map[nr][nc]
        # blue
        if color == 2:
            if second:
                # 2번째라면, r c 그대로
                cnt_map[r][c] = cnt
                horse[i] = [r, c, d_copy, link]
            else:
                # 1번째라면 d 전환
                d += 1
                if d == 3:
                    d = 1
                elif d == 5:
                    d = 3
                # recursive to new r, c
                nr, nc = r + row_dir[d - 1], c + col_dir[d - 1]
                horse, finish = move(horse, i, r, c, nr, nc, d, True, cnt)
        # white, red
        else:
            # adj에 본인 넣기 (link)
            adj.append(i+1)
            # horse 변환
            horse[i] = [nr, nc, d, link]
            # print(cnt_map[r][c], link)
            # link 모두 변환
            while link:
                adj.append(link)
                hr, hc, hd, hlink = horse[link-1]
                # 기존 link도 삭제
                cnt_map[hr][hc].remove(link)
                # link 정보 갱신
                horse[link-1] = [nr, nc, hd, hlink]
                # link 반복
                link = hlink
            # white
            if color == 0:
                # 새로운 좌표에 이미 존재한다면
                if cnt_map[nr][nc]:
                    # connect link
                    # 기존 끝을 새롭게 들어갈 첫 말 링크 주기
                    horse[cnt_map[nr][nc][-1]-1][3] = adj[0]
                # 합치기
                cnt_map[nr][nc] += adj
            # red
            elif color == 1:
                # 새로운 좌표에 이미 존재한다면
                if cnt_map[nr][nc]:
                    # connect link
                    # 기존 끝을 새롭게 들어갈 끝 말 링크 주기 (거꾸로)
                    horse[cnt_map[nr][nc][-1]-1][3] = adj[-1]
                # 합치기
                cnt_map[nr][nc] += adj[::-1]
                # 링크 반대로 주기
                for a in range(len(adj)-1, 0, -1):
                    horse[adj[a]-1][3] = adj[a-1]
                horse[adj[0]-1][3] = 0
            # cnt_map 내에서 중간에 위치할 경우 기존 링크 삭제
            if cnt_map[r][c]:
                horse[cnt_map[r][c][-1] - 1][3] = 0
            # 4개 인접 끝내기
            if len(cnt_map[nr][nc]) >= 4:
                finish = True
    else:
        # N 범위 벗어났을 때
        if second:
            cnt_map[r][c] = cnt
            horse[i] = [r, c, d_copy, link]
        else:
            d += 1
            if d == 3:
                d = 1
            elif d == 5:
                d = 3
            nr, nc = r+row_dir[d-1], c+col_dir[d-1]
            horse, finish = move(horse, i, r, c, nr, nc, d, True, cnt)
    return horse, finish

def one_step():
    global horse
    for i, [r, c, d, l] in enumerate(horse):
        new_r, new_c = r + row_dir[d-1], c + col_dir[d-1]
        cnt_copy = cnt_map[r][c][:]
        cnt_map[r][c].remove(i+1)
        horse, finish = move(horse, i, r, c, new_r, new_c, d, False, cnt_copy)
        # print('horse')
        # print(horse)
        # for a in cnt_map:
        #     for i in a:
        #         print(len(i), end=' ')
        #     print()
        # print()
        if finish:
            return True
    return False


rl = lambda:sys.stdin.readline()

N, K = map(int, rl().split())

chess_map = []
for _ in range(N):
    # 0: white / 1: red / 2:blue
    chess_map.append(list(map(int,rl().split())))

cnt_map = [[[] for i in range(N+1)] for j in range(N+1)]
horse = []
for i in range(K):
    r, c, d = map(int, rl().split())
    cnt_map[r-1][c-1].append(i+1)
    link = 0
    horse.append([r-1, c-1, d, link])

row_dir, col_dir = [0, 0, -1, 1], [1, -1, 0, 0]



t = 0
while t <= 1000:
    # print("before")
    # for a in cnt_map:
    #     print(a)
    finish = one_step()
    # print("after")
    # for a in cnt_map:
    #     print(a)
    # print()
    # print(horse)
    t += 1
    if finish:
        break


if t > 1000:
    print(-1)
else:
    print(t)

