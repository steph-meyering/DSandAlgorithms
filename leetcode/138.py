"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        top = Node(1)
        res = top
        cur = head
        pointers = {}
        while cur:
            curid = id(cur)
            if curid in pointers:
                nxt = pointers[curid]
            else:
                nxt = Node(cur.val)
                pointers[curid] = nxt
            randid = id(cur.random) if cur.random else None
            if randid:
                if randid in pointers:
                    randnode = pointers[randid]
                else:
                    randnode = Node(cur.random.val)
                    pointers[randid] = randnode
                nxt.random = randnode
            top.next = nxt
            top = top.next
            cur = cur.next
            pointers[curid] = nxt
        return res.next
