# 101. Symmetric Tree

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
# @return {Boolean}

def is_symmetric(root)
    return true if !root
    return true if (!root.left && !root.right)
    left_child = root.left
    right_child = root.right
    return helper(left_child, right_child)
end

def helper(left, right)
    return true if (!left && !right)
    return false if (!left || !right)
    return false if left.val != right.val
    helper(left.left, right.right) && helper(left.right, right.left)
end