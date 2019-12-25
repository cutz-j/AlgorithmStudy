import itertools
import sys

# JOSEPHUS
##### k = 1일 경우, 에러 발생 #######
def search(k, arr, remainder):
    n = len(arr)
    if n == 2:
        return arr[0], arr[1]
    dm = []
    for i, element in enumerate(arr):
        if i % k == remainder:
            rem = 2-(n-(i+1))
            continue
        dm.append(element)
    return search(k, dm, rem)

###################################
    
def search_two(n, k):
    survivors = [i for i in range(1, n+1)]
    kill = 0
    while n > 2:
        value = survivors[kill]
        kill = survivors.index(value) # 삭제 index
        value = survivors.pop(kill) # 삭제 value
        n -= 1
        if (kill >= n): # 삭제가 마지막일 경우, value를 첫 번째로
            kill = 0
        for i in range(0, k-1): # 삭제가 진행됐기 때문 2 loop
            if (survivors[kill] == survivors[-1]): # jump 중 요소가 마지막일 s경우, value를 첫 번째로
                kill = -1
            kill += 1
    return survivors[0], survivors[1]


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = [i+1 for i in range(n)]
    r1, r2 = search_two(n, k)
    print("%d %d" %(r1, r2))