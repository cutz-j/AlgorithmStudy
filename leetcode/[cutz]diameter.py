from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return -1

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.res = max(self.res, left + right + 2)
        return max(left, right) + 1

#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         # exception
#         if not root:
#             return 0

#         # left deepest depth + right deepest depth = answer
#         # divide subtree into twos (left-right)
#         sub_tree =[]
#         if root.left:
#             left_sub = root.left
#             sub_tree.append(left_sub)
#         if root.right:
#             right_sub = root.right
#             sub_tree.append(right_sub)

#         ans = []

#         # BFS
#         for sub in sub_tree:
#             queue = deque()
#             depth = 1
#             queue.append((sub, depth))
#             while queue:
#                 node, depth = queue.popleft()
#                 if node.left:
#                     queue.append((node.left, depth+1))
#                 if node.right:
#                     queue.append((node.right, depth+1))
#             ans.append(depth)

#         return sum(ans)


