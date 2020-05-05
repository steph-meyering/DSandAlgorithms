# 965. Univalued Binary Tree

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


# recursive solution 

def is_unival_tree(root)
    return true if !(root)
    if root.left
        return false if root.left.val != root.val
    end
    if root.right
        return false if root.right.val != root.val
    end
    return is_unival_tree(root.right) && is_unival_tree(root.left)
end


# iterative solution

def is_unival_tree(root)
    queue = [root]
    root_val = root.val
    until queue.empty?
        el = queue.shift()
        next if el.nil?
        return false if el.val != root_val
        queue.push(el.left, el.right)
        
    end
    return true
end