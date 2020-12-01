# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev, cur = head, head
        while cur:
            if cur.val == prev.val:
                cur = cur.next
            else:
                prev.next = cur
                prev = cur
        prev.next = None
        return head
