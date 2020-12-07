"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        if root:
            q.append(root)
        while q:
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if i < l - 1:
                    n.next = q[0]
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return root