# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        res = [0] * len(arr)
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return [0]
        stack = [[arr[0], 0]]
        i = 1
        while i < len(arr):
            if len(stack) == 0:
                stack.append([val, i])
                i += 1
                continue
            prev_val = stack[-1][0]
            prev_i = stack[-1][1]
            val = arr[i]
            if val > prev_val:
                res[prev_i] = val
                stack.pop()
            else:
                stack.append([val, i])
                i += 1
        return res
