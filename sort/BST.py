
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.subtree = 0
        
class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root == None
    
    def _insert_value(self, node, data):
        if node == None:
            # root
            node = Node(data)
        else:
            # not root
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    def find(self, data):
        return self._find_value(self.root, data)
    
    def _find_value(self, node, data):
        if node == None or node.data == data:
            return node is not None
        
        elif data < node.data:
            return self._find_value(node.left, data)
        
        else:
            return self._find_value(node.right, data)
        
    def find_min(self):
        return self._find_min(self.root)
    
    def _find_min(self, node):
        if node.left == None:
            return node.data
        
        else:
            return self._find_min(node.left)
        
    def find_max(self):
        return self._find_max(self.root)
    
    def _find_max(self, node):
        if node.right == None:
            return node.data
        
        else:
            return self._find_max(node.right)
                                 
        
#    def next_larger(self, data):
        
# Rank / next_larger
        
                
    