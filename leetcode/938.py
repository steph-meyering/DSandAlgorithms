# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = 0
        self.helper(root, L, R, self.res)
        return self.res

    def helper(self, root, L, R, res):
        if root:
            if root.val >= L and root.val <= R:
                self.res += root.val
                self.helper(root.left, L, R, res)
                self.helper(root.right, L, R, res)
            elif root.val <= L:
                self.helper(root.right, L, R, res)
            elif root.val >= R:
                self.helper(root.left, L, R, res)
