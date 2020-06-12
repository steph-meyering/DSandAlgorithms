/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  let node = root; // 2
  while (node) {
    let largest = Math.max(p.val, q.val); // 4
    let smallest = Math.min(p.val, q.val); // 2
    if (node.val < largest && node.val > smallest) return node;
    if (node.val === largest || node.val === smallest) return node;
    if (largest > node.val && smallest > node.val) {
      node = node.right;
    } else {
      node = node.left;
    }
  }
};
