# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: 
            return 0
        stack = [[root, "R"]]
        counter = 0
        while stack:
            node, pos = stack.pop()
            if not node.left and not node.right and pos == "L":
                counter += node.val
            if node.left:
                stack.append([node.left, "L"])
            if node.right:
                stack.append([node.right, "R"])
        return counter