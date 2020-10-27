#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    dp = defaultdict(int)
    if len(arr) == 1:
        dp[0] = arr[0]
    elif len(arr) == 2:
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
    else:
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        dp[2] = max(arr[2], arr[2]+dp[0], dp[1])
        for i in range(3, len(arr)):
            dp[i] = max(arr[i], arr[i]+dp[i-2], dp[i-1])
    return dp[len(arr)-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
