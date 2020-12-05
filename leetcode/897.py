# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.traversal = []
        self.dfs(root)
        for i, node in enumerate(self.traversal):
            node.left = None
            if i == len(self.traversal) - 1:
                node.right = None
            else:
                node.right = self.traversal[i+1]
        return self.traversal[0]
                
        
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.traversal.append(root)
            self.dfs(root.right)
            