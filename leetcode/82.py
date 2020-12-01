# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        res = None
        res_cur = None
        while cur:
            if prev and prev.val == cur.val:
                pass
            else:
                nxt = cur.next
                if not nxt or nxt.val != cur.val:
                    if not res:
                        res = cur
                        res_cur = res
                    else:
                        res_cur.next = cur
                        res_cur = res_cur.next
            prev = cur
            cur = cur.next
        if res_cur:
            res_cur.next = None
        return res
