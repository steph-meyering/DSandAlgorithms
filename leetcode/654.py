# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root = TreeNode()
        self.helper(root, nums)
        return root

    def helper(self, node, arr):
        val = max(arr)
        node.val = val
        i = arr.index(val)         # index position of subarray max
        left = arr[:i]
        right = []
        if left:
            node.left = TreeNode()
            self.helper(node.left, left)
        if len(arr) != i:
            right = arr[i+1:]
        if right:           # add right child and make recursive call
            node.right = TreeNode()
            self.helper(node.right, right)
