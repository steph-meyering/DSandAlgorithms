// 141. Linked List Cycle

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  let seen = new Set();
  while (head) {
    if (seen.has(head)) {
      return true;
    } else {
      seen.add(head);
    }
    if (head.next) {
      head = head.next;
    } else {
      return false;
    }
  }
  return false;
};
