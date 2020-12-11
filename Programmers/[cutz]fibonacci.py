def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_tab(n):
    dp = {}
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def fib_mem(n):
    if n <= 1:
        return n

    if dp.get(n, -1) != -1:
        return dp[n]

    dp[n] = fib_mem(n-1) + fib_mem(n-2)
    return dp[n]

dp = {}
print(fib_rec(10))
print(fib_tab(10))
print(fib_mem(10))