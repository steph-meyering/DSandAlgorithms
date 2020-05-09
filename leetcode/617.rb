# 617. Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} t1
# @param {TreeNode} t2
# @return {TreeNode}

# def merge_trees(t1, t2)
#     output = TreeNode.new
#     output = helper(t1, t2)
# end

def merge_trees(node1, node2)
    return nil if (!node1 && !node2)
    return node1 if !node2
    return node2 if !node1
    new_node = TreeNode.new()
    new_node.val = node1.val + node2.val
    new_node.left = merge_trees(node1.left, node2.left)
    new_node.right = merge_trees(node1.right, node2.right)
    return new_node
end