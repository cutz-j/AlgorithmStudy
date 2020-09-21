import sys

def check(arr):
    ans = True
    before = False
    previous = arr[0]
    consec = [arr[0]]
    for i in arr[1:]:
        if abs(previous - i) > 1:
            ans = False
            break
        elif previous != i:
            if before:
                if len(consec) >= L:
                    for _ in range(L):
                        consec.pop()
                    before = False
                else:
                    ans = False
                    break
            if previous < i:
                # 이전 수가 이후보다 1 작을 경우
                if len(consec) < L:
                    ans = False
                    break
                else:
                    consec = []
            else:
                # 이전 수가 이후보다 1 클 경우
                before = True
                consec = []
            consec.append(i)
            previous = i
        else:
            # 동일할 경우
            consec.append(i)
    if before and len(consec) < L:
        ans = False
    return ans



rl = lambda: sys.stdin.readline()

N, L = map(int, rl().split())
all_map = []
for _ in range(N):
    all_map.append(list(map(int, rl().split())))

cnt = 0
# row check
for i in range(N):
    ans = check(all_map[i])
    if ans:
        cnt += 1


for i in range(N):
    col = []
    for j in range(N):
        col.append(all_map[j][i])
    ans = check(col)
    if ans:
        cnt += 1


print(cnt)