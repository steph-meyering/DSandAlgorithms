"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            l = len(q)
            level = []
            for _ in range(l):
                n = q.popleft()
                level.append(n.val)
                if n.children:
                    q += n.children
            res.append(level)
        return res
