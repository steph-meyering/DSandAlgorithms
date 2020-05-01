/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */

/* 
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Input:
          1
        /   \
       2     3
     /  \   / \
    4    5 N   N
4 -> ["4"]
5 -> ["5"]
2 -> ["2->4", "2->5"]
    ["1->2->4", "1->2->5"]


Output: ["1->2->4", "1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
*/

const binaryTreePaths = function (node) {
  // root => (1)
  if (!node.left && !node.right) return [`${node.val}`]; // ["3"]

  let l = [];
  let r = [];

  if (node.left) {
    l = binaryTreePaths(node.left); // ["2->4", "2->5"];
  } else if (node.right) {
    r = binaryTreePaths(node.right); // ["3"]
  }

  let combined = l.concat(r); // ["1->2->4", "1->2->5", "1->3"];

  return combined.map((path) => node.val + "->" + path);
};
