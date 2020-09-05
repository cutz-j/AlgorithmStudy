#!/bin/python3

import math
import os
import random
import re
import sys

def binary_search(left, right, n):
    print(left, right, n)
    if left == right:
        return left, False
    
    mid = (left+right)//2
    
    middle = scores[mid]
    if middle == n:
        return mid, True
    
    elif middle > n:
        return binary_search(mid+1, right, n)
    
    elif middle < n:
        return binary_search(left, mid, n)
        


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    answer = []
    ranking = 1
    rank_list = []
    
    for i in range(len(scores)-1):
        next_s, s = scores[i+1], scores[i]
        if next_s != s:
            rank_list.append(ranking)
            ranking += 1
        else:
            rank_list.append(ranking)
    rank_list.append(ranking)
    
    for a in alice:
        alice_idx, same = binary_search(0, len(scores), a)
        if same:
            answer.append(rank_list[alice_idx])
        else:
            if 0 <= alice_idx < len(scores):
                answer.append(rank_list[alice_idx])
            else:
                answer.append(rank_list[alice_idx-1]+1)
    return answer
    

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
6