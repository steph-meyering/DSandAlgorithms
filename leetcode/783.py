# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        in_order = []
        min_diff = float('inf')
        self.dfs(root, in_order)
        for i in range(len(in_order) - 1):
            min_diff = min(min_diff, in_order[i+1] - in_order[i])
        return min_diff

    def dfs(self, node, res):
        if node:
            self.dfs(node.left, res)
            res.append(node.val)
            self.dfs(node.right, res)
