import sys

def solution(routes):
    # routes: 차량 경로
    # 모든 차량이 한번은 단속용 카메라를 만나도록 하는 최소 카메라 대수
    answer = 0
    sorted_routes = sorted(routes, key=lambda x: x[1])
    start, end = -sys.maxsize, -sys.maxsize
    for s, e in sorted_routes:
        if s > end:
            answer += 1
            end = e
    return answer