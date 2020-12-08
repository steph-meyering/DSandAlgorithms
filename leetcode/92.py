# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        rev_len = n - m
        if rev_len < 1:
            return head
        pos = 1
        cur, prev = head, head
        while pos < m:
            prev = cur
            cur = cur.next
            pos += 1
        if m == 1:
            return self.reverse(cur, rev_len)
        else:
            prev.next = self.reverse(cur, rev_len)
        return head

    def reverse(self, head, k):
        prev = None
        cur = head
        for _ in range(k+1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        head.next = cur
        return prev
