import sys

c = 6 & (4 == 4)
d = (6 & 4) == 4

full_pizza = (1 << 20) - 1

# 에라토스테네스의 체

MAX_N = 50

sieve = [255 for i in range(int((MAX_N+7)/8))]


def is_prime(k):
    return sieve[k >> 3] & 1 << (k & 7)

def set_composite(k):
    sieve[k >> 3] = sieve[k >> 3] & ~(1 << (k & 7))

# 64비트 정수 배열

def get(mask, idx):
    return (mask >> (idx << 2)) & 15 # % 16

def set_(mask, idx, value):
    return mask & ~(15 << (idx << 2)) | (value << (idx << 2))

# 극대안정집합
    
