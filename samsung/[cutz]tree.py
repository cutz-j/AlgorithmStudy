def spring_summer(): #봄, 여름 함수
    global soils
    global trees
    dead_trees = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            trees[i][j].sort()
            for idx in range(len((trees[i][j]))):
                if soils[i][j]>= trees[i][j][idx]:
                    soils[i][j] -= trees[i][j][idx]
                    trees[i][j][idx] += 1
                else:
                    dead_trees[i][j].append(idx)
            for idx in range(len(dead_trees[i][j])-1,-1,-1): #죽은 나무가 있을 경우 해당 칸 안만 바뀌기 때문에 칸별로 봄여름을 한번에 진행했다. 
                temp = trees[i][j][dead_trees[i][j][idx]]
                del trees[i][j][dead_trees[i][j][idx]]
                soils[i][j] += temp//2
    return


delta = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]


def autumn(): #가을 함수
    new_trees = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for tree in trees[i][j]:
                if tree%5 == 0:
                    for dl in delta:
                        newi = i + dl[0]
                        newj = j + dl[1]
                        if -1<newi<N and -1<newj<N:
                            new_trees[newi][newj].append(1)
    for i in range(N):
        for j in range(N):
            trees[i][j].extend(new_trees[i][j])
    return


def winter(): #겨울함수
    for i in range(N):
        for j in range(N):
            soils[i][j] +=fertilizer[i][j]
    return


N, M, K = map(int, input().split())
fertilizer = [list(map(int, input().split())) for _ in range(N)]
soils = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)
for _ in range(K):
    spring_summer()
    autumn()
    winter()
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])

print(ans)