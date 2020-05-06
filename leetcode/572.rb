# 572. Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} s
# @param {TreeNode} t
# @return {Boolean}
def is_subtree(s, t)
    tree = dfs(s)
    target = dfs(t)
    p tree
    p target
    # dfs t
    # dfs s     
    # check s for inclusivity of t
    
    
end

def dfs(root)
    return [root.val] if !root
    return [root.val] if (!root.left && !root.right) 
    left = dfs(root.left)
    right = dfs(root.right)
    return left + right + [nil] + [root.val]
end