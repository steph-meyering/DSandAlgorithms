# 199. Binary Tree Right Side View

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
# @return {Integer[]}

def right_side_view(root)
    return [] if !root
    output = []
    queue = [[root, 0]]
    until queue.empty?
        node, level  = queue.shift
        if output[level]
            output[level].push(node.val)
        else
            output[level] = [node.val]
        end
        queue.push([node.left, level + 1]) if node.left
        queue.push([node.right, level + 1]) if node.right
    end
    res = []
    output.each do |level|
        res << level[-1]
    end
    res
end