Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
  # iterative
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack = [[root, 0]]
        res = []
        while stack:
            node, depth = stack.pop()
            if len(res) == depth:
                res.append([0, 0])
            res[depth][0] += node.val
            res[depth][1] += 1
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        for i, pair in enumerate(res):
            total, div = pair
            res[i] = total / div
        return res
