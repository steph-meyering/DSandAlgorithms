# 590. N-ary Tree Postorder Traversal

# Definition for a Node.
# class Node
#     attr_accessor :val, :children
#     def initialize(val)
#         @val = val
#         @children = []
#     end
# end

# @param {Node} root
# @return {List[int]}

def postorder(root)
    return [] if !root
    return [root.val] if root.children.empty?
    output = [] #[5,6,3,2]
    root.children.each do |child|
        output += postorder(child)
    end
    output += [root.val]
    return output
end