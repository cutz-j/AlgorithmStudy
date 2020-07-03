import sys

# 1,2,3,4분면의 차이

def Z(size, y, x):
    global cnt
    if size == 2: # 최소 단위 basis
        if y==r and x==c: # 왼쪽 상단
            print(cnt)
            return
        
        cnt += 1
        if y==r and x+1==c: # 우측 상단
            print(cnt)
            return
            
        cnt += 1
        if y+1==r and x==c: # 좌측 하단
            print(cnt)
            return
        
        cnt += 1
        if y+1==r and x+1==c: # 우측 하단
            print(cnt)
            return
        
        cnt += 1 # 해당 size에서 없을 경우, cnt + 4
        return
    
    # recursive 1/2/3/4분면
    # 연산자 우선순위 주의!
    # 1분면
    Z(size>>1, y, x)
    # 2분면
    Z(size>>1, y, x+(size>>1))
    # 3분면
    Z(size>>1, y+(size>>1), x)
    # 4분면
    Z(size>>1, y+(size>>1), x+(size>>1))
    
        
        
        

#rl = lambda: sys.stdin.readline()
rl = input

N, r, c = map(int, rl().split())
cnt = 0

Z(1 << N, 0, 0)