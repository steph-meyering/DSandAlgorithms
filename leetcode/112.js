/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {boolean}
 */
var hasPathSum = function (root, sum, curSum = 0) {
  if (!root) return false;
  curSum += root.val;
  if (!root.right && !root.left && sum === curSum) return true;
  return (
    hasPathSum(root.left, sum, curSum) || hasPathSum(root.right, sum, curSum)
  );
};
