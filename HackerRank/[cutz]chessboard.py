#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    answer = []
    for a in range(1, n):
        res = []
        for b in range(1, a+1):
            if a == b == n-1:
                res.append(1)
                continue

            queue = deque()
            visited = [[0 for _ in range(n)] for __ in range(n)]
            queue.append((0, 0, 0))
            end = sys.maxsize
            if a == b:
                step = [(a, b), (a, -b), (-a, b), (-a, -b)]
            else:
                step = [(a, b), (a, -b), (-a, b), (-a, -b),
                        (b, a), (b, -a), (-b, a), (-b, -a)]

            while queue:
                row, col, cnt = queue.popleft()
                if cnt > end:
                    continue

                visited[row][col] = 1

                for i, j in step:
                    new_row, new_col = row+i, col+j
                    if (0 <= new_row < n) and (0 <= new_col < n):
                        if new_row == new_col == n-1:
                                if cnt+1 < end:
                                    end = cnt+1
                                continue
                        if visited[new_row][new_col] == 0:
                            if cnt+1 < end:
                                queue.append((new_row, new_col, cnt+1))
                          
            if end != sys.maxsize:
                res.append(end)
            else:
                res.append(-1)
        answer.append(res)
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    for i in range(n-1):
        row = result[i]
        for j in range(len(row), n-1):
            row.append(result[j][i])
        fptr.write(' '.join(map(str, row)))
        fptr.write('\n')
    fptr.close()
