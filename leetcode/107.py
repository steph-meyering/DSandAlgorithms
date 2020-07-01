# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        q = [[root, 0]]
        while q:
            node, i = q.pop()
            if node.right:
                q.append([node.right, i+1])
            if node.left:
                q.append([node.left, i+1])
            if len(res) == i:
                res.append([])
            res[i].append(node.val)
        return res[::-1]
