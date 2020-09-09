#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    if k == 0:
        return n*m
    
    track = sorted(track)
    row_dict = {}
    previous = track[0][0]
    answer = 0
    for r, c_start, c_end in track:
        if previous != r:
            answer += m - (row_dict[previous][1]-row_dict[previous][0]+1) + row_dict[previous][2]

        if row_dict.get(r, []):
            prev_s, prev_e, med = row_dict[r]
            if prev_e < c_start:
                row_dict[r] = [prev_s, c_end, med+(c_end-prev_e-1)]
            else:
                row_dict[r] = [min(prev_s, c_start), max(prev_e, c_end), med]
        else:
            row_dict[r] = [c_start, c_end, 0]
        
        previous = r
    
    answer += m - (row_dict[previous][1]-row_dict[previous][0]+1)+row_dict[previous][2]

    answer += (n-len(row_dict))*m
    
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
