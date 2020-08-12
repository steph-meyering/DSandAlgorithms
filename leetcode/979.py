# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        self.helper(root)
        return self.moves

    def helper(self, root):
        if root:
            left = self.helper(root.left) or 0
            right = self.helper(root.right) or 0
            self.moves += abs(left) + abs(right)
            return root.val + left + right - 1
