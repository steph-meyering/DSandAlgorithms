# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pstack = [p]
        qstack = [q]
        while pstack or qstack:
            pnode = pstack.pop()
            qnode = qstack.pop()
            if bool(qnode) != bool(pnode):
                return False
            if bool(qnode) != False and qnode.val != pnode.val:
                return False
            if pnode:
                pstack.extend([pnode.left, pnode.right])
            if qnode:
                qstack.extend([qnode.left, qnode.right])
        return True