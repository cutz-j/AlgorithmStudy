#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n, res):
    # basis
    if n==0:
        return res
    
    result = extraLongFactorials(n-1, res*n)
    return result

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n, 1))
