# 노드 생성
class Node(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.left = self.right = None

# 이중검색트리 생성
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    #insert
    def insert(self, p ,q):
        self.root = self._insert_value(self.root, p, q)
        return self.root is not None

    def _insert_value(self, node, p, q):
        if node is None:
            node = Node(p, q)
        else:
            if p <= node.p:
                node.left = self._insert_value(node.left, p)
            else:
                node.right = self._insert_value(node.right, p)
        return node

    #find
    def ind(self, key):
        return self._find_value(self.root, key)

    def _fine_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    #delete
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                #
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted


if __name__ == "__main__":
    for _ in range(int(input())):

        N = int(input())
        result = 0
        bst = BinarySearchTree()

        for _ in range(N):
            p, q = map