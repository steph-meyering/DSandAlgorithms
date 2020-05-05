# 226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {TreeNode}

def invert_tree(root)
    return root if  !root || (!root.left && !root.right)
    temp = root.left
    root.left = invert_tree(root.right)
    root.right = invert_tree(temp)
    return root
end