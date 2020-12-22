# Iterative solution
#
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)
        d = 0
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            d += 1
        return d

# Recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
