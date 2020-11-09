# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, root.val, root.val)
        return self.res

    def dfs(self, root, node_max, node_min):
        if root:
            node_max = max(root.val, node_max)
            node_min = min(root.val, node_min)
            self.res = max(self.res, abs(node_max - node_min))
            self.dfs(root.left, node_max, node_min)
            self.dfs(root.right, node_max, node_min)
