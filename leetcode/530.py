# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []
        self.dfs(root, res)
        smallest_difference = float('inf')
        for i in range(len(res) - 1):
            smallest_difference = min(
                abs(res[i] - res[i+1]), smallest_difference)
        return smallest_difference

    def dfs(self, node, res):
        if node:
            self.dfs(node.left, res)
            res.append(node.val)
            self.dfs(node.right, res)
