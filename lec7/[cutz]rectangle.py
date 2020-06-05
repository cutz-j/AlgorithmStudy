import sys


# def solve(left, right):
#     # [left, right] 구간에서의 가장 큰 넓이 반환
#     if left == right:
#         return hist[left] # 1개 남은 경우
#
#     mid = (left + right) // 2 # [left, mid] [mid+1, right] divide
#     # 더 큰 넓이
#     result = max(solve(left, mid), solve(mid+1, right))
#
#     # calculate area: 걸쳐있는 경우
#     lo, hi = mid, mid+1
#     height = min(hist[lo], hist[hi])
#
#     # [1, 1]일 경우에는 2이기 때문에, 2로 지정
#     result = max(result, height*2)
#
#     # 반복하여 확장
#     while left < lo or hi < right:
#         if hi < right and (lo == left or hist[lo-1] < hist[hi+1]):
#             hi += 1
#             height = min(height, hist[hi])
#
#         else:
#             lo -= 1
#             height = min(height, hist[lo])
#
#         result = max(result, height * (hi - lo +1))
#     return result
        

    

#rl = lambda: sys.stdin.readline()
rl = input

while True:
    N, *hist = list(map(int, rl().split()))
    hist.append(0)
    if N == 0:
        break
    s = []
    a = 0
    for i, h in enumerate(hist):
        while s and hist[s[-1]] > h:
            ih = hist[s.pop()]
            w = i - s[-1] - 1 if s else i
            if a < w * ih:
                a = w * ih
        s.append(i)
    print(a)
