# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        b = "0b"
        while head:
            b += str(head.val)
            head = head.next
        return int(b, 2)
