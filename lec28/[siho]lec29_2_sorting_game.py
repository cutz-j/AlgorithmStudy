import sys
from queue import Queue
from collections import deque


def precalc(n):
    global toSort

    # Initialization
    toSort[perm_str] = 0
    q = Queue()
    q.put(perm_str)
    while not q.empty():

        here = q.get()  # equivalent to .pop(0)
        cost = toSort[here]
        for i in range(n):
            for j in range(i + 2, n + 1):

                # Reverse elements in range(i, j)
                here_reverse = here[:i] + here[i:j][::-1] + here[j:]
                if here_reverse not in toSort:
                    toSort[here_reverse] = cost + 1
                    q.put(here_reverse)


def solve(perm):
    if perm == sorted(perm):
        return 0

    # Initialization
    n = len(perm)
    fixed = [None] * n
    for i in range(n):

        smaller = 0
        for j in range(n):

            if perm[j] < perm[i]:
                smaller += 1

        fixed[i] = smaller

    fixed_str = ''.join(str(i) for i in fixed)

    return toSort[fixed_str]


input_ = lambda: sys.stdin.readline()
if __name__ == '__main__':

    C = int(input_())
    for _ in range(C):
        n = int(input_())
        perm = list(map(int, input_().split()))
        perm_str = ''.join(str(i) for i in range(n))

        toSort = dict()
        precalc(n)
        print(solve(perm))
