import sys
    

#rl = lambda: sys.stdin.readline()
rl = input

len_stair = int(rl())
stair = [int(rl()) for _ in range(len_stair)]
dp = [0 for _ in range(len(stair))]

if len(stair) == 1:
    dp[0] = stair[0]

elif len(stair) == 2:
    dp[0] = stair[0]
    dp[1] = max(stair[0]+stair[1], stair[1])

else:
    dp[0] = stair[0]
    dp[1] = max(stair[0]+stair[1], stair[1])
    dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])
    
    for i in range(3, len(stair)):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])
    

print(dp[-1])