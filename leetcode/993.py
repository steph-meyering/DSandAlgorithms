# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = [[root, None, 0]]
        resx = []
        resy = []
        while q:
            node, parent, depth = q.pop()
            if node.left:
                q.append([node.left, node, depth + 1])
            if node.right:
                q.append([node.right, node, depth + 1])
            if node.val == x:
                resx = [parent, depth]
            if node.val == y:
                resy = [parent, depth]
            if resx and resy:
                return resx[0] != resy[0] and resx[1] == resy[1]
