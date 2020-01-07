# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 23:46:22 2020

@author: samle
"""

#input
num_test = int(input())
num_node = int(input())

node_pre = []
node_inord = []

   
for _ in range(num_node):
    node_pre.append(input())

for _ in range(num_node):
    node_inord.append((input()))


    
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None  
        
class Tree(object):    
    def insert(self,data):
        if (self.data is None) & (self.data is data.left):
            self.left = Node(data)
        
        elif (self.data is None) & (self.data == data.right):
            self.right = Node(data)
            
        else:
            self.data = data
          
    def InOrder(self,root):
        ''' Left -> Root -> right '''
        res = []
        if root:
            res = self.InOrder(root.left)
            res.append(root.data)
            res = res + self.InOrder(root.right)
        return res
    
    def PreOrder(self,root):
        ''' Root -> Left -> right '''
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreOrder(root.left)
            res = res + self.PreOrder(root.right)
        return res
    
    def PostOrder(self,root):
        ''' Left -> Right -> Root '''
        res = []
        if root:
            res = self.PostOrder(root.left)
            res = res + self.PostOrder(root.right)
            res.append(root.data)
        return res


if __name__ == '__main__':        
    root = Node(node_pre[0])
    root_idx = node_inord.index(node_pre[0])
    right = list(reversed(node_inord[:root_idx]))
    left = node_inord[root_idx+1:]
    
    for r in right:
        root.insert(InOrder(r))
    
    for l in left:
        root.insert(InOrder(l))
    
    
    

    



        
    