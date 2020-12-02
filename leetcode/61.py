# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0 :
            return head
        tail = head
        cur = head
        size = 1
        while cur and cur.next:
            size += 1
            cur = cur.next
        cur.next = head
        for _ in range(size - (k % size) - 1):
            tail = tail.next
        res = tail.next
        tail.next = None
        return res