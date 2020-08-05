# Recursive

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         res = []
#         self.helper(root, res)
#         return res

#     def helper(self, root, res):
#         if root:
#             res.append(root.val)
#             for node in root.children:
#                 self.helper(node, res)

# Iterative

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return res
