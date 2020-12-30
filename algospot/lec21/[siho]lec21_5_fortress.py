'''
URL: https://algospot.com/judge/problem/read/FORTRESS#
'''

import sys


class Fortress(object):

    def __init__(self, x, y, r):

        self.x = x
        self.y = y
        self.r = r
        self.children = []

    def __repr__(self):
        
        return self.children
        # return '[x: {}, y: {}, r: {}]'.format(self.x, self.y, self.r)
    
    def sqr_(self, n):
        
        return n*n
    
    def sqr_dist(self, fortress):

        return self.sqr_(self.x - fortress.x) + self.sqr_(self.y - fortress.y)
    
    def isChild(self, fortress):
        
        return self.r > fortress.r and self.sqr_(self.r - fortress.r) > self.sqr_dist(fortress)
    
    def addChild(self, fortress):
        
        for child in self.children:
            
            if child.isChild(fortress):
                child.addChild(fortress)
                return
        
        self.children.append(fortress)
    
    def height(self, longest):
        
        h1, h2 = 0, 0
        for child in self.children:
            
            h2 = max(h2, child.height(longest)+1)
            if h2 > h1:
                h1, h2 = h2, h1
        
        longest[0] = max(longest[0], h1, h2)
        return h1


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

            if root.isChild(node):
                root.addChild(node)

        longest = [0]
        root.height(longest)
        print(longest[0])
