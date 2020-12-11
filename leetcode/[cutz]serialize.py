from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))

                queue.append(node.left)
                queue.append(node.right)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#':
            return None
        queue = deque()
        data = data.split()

        root = TreeNode(int(data[0]))
        queue.append(root)
        index = 1

        while queue:
            node = queue.popleft()
            if data[index] is not '#':
                node.left = TreeNode(int(data[index]))
                queue.append(node.left)
            index += 1

            if data[index] is not '#':
                node.right = TreeNode(int(data[index]))
                queue.append(node.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))