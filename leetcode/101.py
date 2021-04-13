# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left) if node.left else queue.append(None)
                    queue.append(node.right) if node.right else queue.append(None)
                else:
                    level.append(None)
            i, j = 0, len(level) - 1
            while i <= j:
                if level[i] != level[j]:
                    return False
                i += 1
                j -= 1
        return True