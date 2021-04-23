# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = deque([root])
        while queue:
            level_total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_total += node.val
                if node.left: queue.append(node.left) 
                if node.right: queue.append(node.right)
            if len(queue) == 0:
                return level_total
    
                