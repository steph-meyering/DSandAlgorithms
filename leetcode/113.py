# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        self.res = []
        self.dfs(root, s, [])
        return self.res

    def dfs(self, root, s, path):
        if root:
            path.append(root.val)
            if not root.left and not root.right and s == root.val:
                return self.res.append(path[:])
            self.dfs(root.left, s - root.val, path)
            self.dfs(root.right, s - root.val, path)