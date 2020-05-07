# 230. Kth Smallest Element in a BST

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
# @param {Integer} k
# @return {Integer}
def kth_smallest(root, k)
    res = in_order(root)
    res[k-1]
end

# in order
def in_order(root, res = []) 
    if root
        in_order(root.left, res)
        res.push(root.val)
        in_order(root.right, res)
    end
    return res
end

# post order
def post_order(root, res = [2,1,4,3]) 
    if root
        post_order(root.left, res)
        post_order(root.right, res)
        res.push(root.val)
        
    end
    return res
end


# post order
def pre_order(root, res = [3,1,2,4]) 
    if root
        res.push(root.val)
        pre_order(root.left, res)
        pre_order(root.right, res)
    end
    return res
end