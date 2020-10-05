# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        t1 = []
        t2 = []
        res = []
        self.traverse(root1, t1)
        self.traverse(root2, t2)
        i, j = 0, 0
        while i < len(t1) and j < len(t2):
            if t1[i] < t2[j]:
                res.append(t1[i])
                i += 1
            else:
                res.append(t2[j])
                j += 1
        res = res + t1[i:] + t2[j:]
        return res

    def traverse(self, root, t):
        if root:
            self.traverse(root.left, t)
            t.append(root.val)
            self.traverse(root.right, t)
