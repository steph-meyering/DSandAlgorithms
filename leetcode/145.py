# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#  RECURSIVE:
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
# if not root:
#     return []
# return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

# ITERATIVE:
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return reversed(res)
