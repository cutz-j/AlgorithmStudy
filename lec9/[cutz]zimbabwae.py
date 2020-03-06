import sys

# guess prior price

n,m  = -1, -1
e, digits = '', ''

def generate(price, taken):
    if len(price) == n:
        if price < e:
            print(price)
        return
    
    for i in range(n):
        if (taken[i]==False) and (i==0 or digits[i-1]!=digits[i] or taken[i-1]):
            taken[i] = True
            generate(price + digits[i], taken)
            taken[i] = False
            
MOD = 1000000007
cache = [[[-1 for _ in range(2)] for __ in range(20)] for ___ in range(1<<14)]

def price(index, taken, mod, less):
    if index == n:
        return 1 if less and mod == 0 else 0
    
    ret = cache[taken][mod][less]
    if ret != -1:
        return ret
    
    ret = 0
    for i in range(n):
        if taken==True and e[index] < digits[i]:
            if less == False and e[index] < digits[i]:
                continue
            
            if (i > 0 and digits[i-1]==digits[i] and (taken==True and (1<<(i-1)))==0):
                continue
            
            next_taken = taken or (1<<i)
            next_mod = (mod * 10 + digits[i] - '0') % m
            next_loss = less or e[index] > digits[i]
            ret += price(index+1, next_taken, next_mod, next_less)
            ret %= MOD
            cache.append(ret)