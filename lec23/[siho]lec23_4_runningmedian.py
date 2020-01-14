'''
URL: https://www.algospot.com/judge/problem/read/RUNNINGMEDIAN
'''

import heapq
import sys

class min_heap():

    def __init__(self):

        self.heap = []
        self.size = 0

    def insert_(self, value):

        heapq.heappush(self.heap, value)
        self.size += 1

    def top(self):

        return self.heap[0]

    def delete_min(self):

        self.size -= 1
        return heapq.heappop(self.heap)

class max_heap():

    def __init__(self):

        self.heap = []
        self.size = 0

    def insert_(self, value):

        heapq.heappush(self.heap, -value)
        self.size += 1

    def top(self):

        return -self.heap[0]

    def delete_min(self):

        self.size -= 1
        return -heapq.heappop(self.heap)


class med_heap():

    def __init__(self):

        self.greater = min_heap()
        self.less = max_heap()
        self.size = 0

    def insert_(self, value):

        if self.greater.size == self.less.size:
            self.less.insert_(value)
        else:
            self.greater.insert_(value)

        if self.greater.size > 0 and self.greater.top() < self.less.top():
            self.greater.insert_(self.less.delete_min())
            self.less.insert_(self.greater.delete_min())

    def median_(self):

        return self.less.top()


input_ = lambda: sys.stdin.readline()
if __name__ == '__main__':
    C = int(input_())
    divisor = 20090711
    for _ in range(C):

        N, a, b = map(int, input_().split())
        A = [None]*N
        A[0] = 1983
        for i in range(1, N):

            A[i] = (A[i-1]*a + b) % divisor

        ret = 0
        heap = med_heap()
        for i in range(N):

            heap.insert_(A[i])
            ret += heap.median_()

        print(ret % divisor)
