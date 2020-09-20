
class Node:
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right
        

class AVL():
    def __init__(self):
        self.root = None
        
    def height(self, n):
        if n == None:
            return 0
        return n.height
    
    def balancefactor(self, n):
        return self.height(n.left) - self.height(n.right)
        
    def rebalance(self, n):
        if self.balancefactor(n) > 1:
            # left node의 높이가 높음
            if self.balancefactor(n.left) < 0:
                # LR회전 필요: 부분 RR회전 --> LL회전
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)
        elif self.balancefactor(n) < -1:
            # right node의 높이가 높음
            if self.balancefactor(n.right) > 0:
                # RL회전 필요: 부분 LL회전 --> RR회전
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
        return n
    
    def rotate_left(self, n):
        # RR회전
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right))+1
        x.height = max(self.height(x.left), self.height(x.right))+1
        return x
        
    def rotate_right(self, n):
        # LL회전
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right))+1
        x.height = max(self.height(x.left), self.height(x.right))+1
        return x
        
     
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
    
    def _insert(self, n, key, value):
        if n == None:
            return Node(key, value, 1)
        if n.key > key:
            n.left = self._insert(n.left, key, value)
        elif n.key < key:
            n.right = self._insert(n.right, key, value)
        else:
            n.value = value
            return n
        n.height = max(self.height(n.left), self.height(n.right))+1
        return self.rebalance(n)
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
        
    def _delete(self, n, key):
        if n == None:
            return None
        
        if n.key > key:
            n.left = self._delete(n.left, key)
        elif n.key < key:
            n.right = self._delete(n.right, key)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n
            n = self._find_min(target.right)
            n.right = self._delete_min(target.right)
            n.left = target.left
        n.height = max(self.height(n.left), self.height(n.right))+1
        return self.rebalance(n)
            
    def find_min(self):
        min_n = self._find_min(self.root)
        return min_n.value
    
    def _find_min(self, n):
        if n.left == None:
            return n
        return self._find_min(n.left)
    
    def delete_min(self):
        return self._delete_min(self.root)
    
    def _delete_min(self, n):
        if n.left == None:
            return n.right
        n.left = self._delete_min(n.left)
        n.height = max(self.height(n.left), self.height(n.right))+1
        return self.rebalance(n)
        
    def preorder(self, n):
        print(n.key)
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)
        
    