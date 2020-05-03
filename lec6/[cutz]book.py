import sys

# 시간 초과 --> maximun 10억: 1억에 1초 --> linear일 경우 10초
def book(N):
    if N == 0:
        return
    
    for i in range(10):
        cnt[i] += str(N).count(str(i))
        
    book(N-1)
    
    
# 전환
def book_recursive(start, end, ten):
    while start%10 != 0 and start <= end:
        for i in range(10):
            cnt[i] += str(start).count(str(i)) * ten
        start += 1
        
    if start > end:
        return
    
    while end%10 != 9 and start <= end:
        for i in range(10):
            cnt[i] += str(end).count(str(i)) * ten
        end -= 1
        
    start_others = int(start/10)
    end_others = int(end/10)
    
    for i in range(10):
        cnt[i] += (end_others - start_others + 1) * ten
        
    book_recursive(start_others, end_others, ten*10)
    

#rl = lambda: sys.stdin.readline()
rl = input

N = int(rl())

cnt = [0 for i in range(10)]
book_recursive(1, N, 1)
for i in range(len(cnt)-1):
    print(cnt[i], end=' ')
print(cnt[-1])