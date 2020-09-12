#!/bin/python3

import math
import os
import random
import re
import sys

class Node(object):
    def __init__(self, gene, health, index):
        self.value = gene
        self.health = health
        self.index = index
        self.is_terminal = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = Node(None, None, None)
        
    def insert(self, genes, health):
        for idx, char in enumerate(genes):
            curr_node = self.root
            for c in char:
                if not curr_node.children.get(c, []):
                    new_node = Node(c, health[idx], idx)
                    curr_node.children[c] = new_node
                curr_node = curr_node.children[c]
            curr_node.is_terminal = True
    
    def search(self, x):
        curr_node = self.head
        for char in x:
            if curr_node.children.get(char, []):
               curr_node = curr_node.chiledren[char]
            else:
                return False
        if curr_node.data:
            return True
    
if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))
    trie = Trie()
    trie.insert(genes, health)
    print(trie.root.children['a'].children['a'].is_terminal)
    s = int(input())

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]
    
    # trie --> insert --> condition serach

    