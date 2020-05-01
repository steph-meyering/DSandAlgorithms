# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def delete_duplicates(head)
    output = head
    while (head && head.next)
        if head.val == head.next.val
            head.next = head.next.next
        else
            head = head.next
        end
    end
    output
end