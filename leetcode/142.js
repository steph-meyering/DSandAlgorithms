/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
  if (!head || !head.next) return null;
  let slow = head;
  let fast = head.next;
  while (slow !== fast) {
    if (!fast.next || !fast.next.next) return null;
    slow = slow.next;
    fast = fast.next.next;
  }
  fast = fast.next;
  let lenCycle = 1;
  while (slow !== fast) {
    fast = fast.next;
    lenCycle++;
  }
  slow = head;
  fast = head;
  for (let i = 0; i < lenCycle; i++) {
    fast = fast.next;
  }
  while (slow !== fast) {
    slow = slow.next;
    fast = fast.next;
  }
  return slow;
};
