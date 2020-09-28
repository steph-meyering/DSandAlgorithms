# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        self.parents = []
        self.dfs(root)
        for parent in self.parents:
            if parent.left:
                res += parent.left.val
            if parent.right:
                res += parent.right.val
        return res

    def dfs(self, root: TreeNode):
        if root:
            if root.val % 2 == 0:
                if root.right:
                    self.parents.append(root.right)
                if root.left:
                    self.parents.append(root.left)
            self.dfs(root.right)
            self.dfs(root.left)
