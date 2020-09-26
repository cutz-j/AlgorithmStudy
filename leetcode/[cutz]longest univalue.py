# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if node.left and node.left.val == node.val:
            left += 1
        else:
            left = 0
        if node.right and node.right.val == node.val:
            right += 1
        else:
            right = 0

        self.res = max(self.res, left + right)
        return max(left, right)
