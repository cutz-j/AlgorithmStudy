'''
URL: https://algospot.com/judge/problem/read/FORTRESS#
'''

import sys


def sqrt_(x):

    return x*x


class Fortress(object):

    def __init__(self, x, y, r):

        self.x = x
        self.y = y
        self.r = r
        self.children = []

    def __repr__(self):

        return '[x: {}, y: {}, r: {}]'.format(self.x, self.y, self.r)

    def sqr_dist(self, fortress):

        return sqrt_(self.x - fortress.x) + sqrt_(self.y - fortress.y)

    def encloses(self, fortress):

        return self.r > fortress.r and sqrt_(self.r - fortress.r) > self.sqr_dist(fortress)

    def isParent(self, fortress):

        return True if self.encloses(fortress) else False

    def insert(self, fortress):

        for child in self.children:

            if child.isParent(fortress):
                child.insert(fortress)
                return

        self.children.append(fortress)

    # TODO
    def get_height(self): return
    def max_height(self): return


input_ = lambda: sys.stdin.readline()
if __name__ == '__main__':
    for _ in range(int(input_())):

        N = int(input_())
        fortress_list = []
        for _ in range(N):

            x, y, r = map(int, input_().split())
            fortress_list.append(Fortress(x, y, r))

        fortress_list.sort(key=lambda fortress: fortress.r, reverse=True)
        root = fortress_list.pop(0)
        for node in fortress_list:

            if root.isParent(node):
                root.insert(node)

        # TODO
        # ...
