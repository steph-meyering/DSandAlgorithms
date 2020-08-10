# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        stack = [s]
        while stack:
            node = stack.pop()
            if node.val == t.val:
                s_stack = [node]
                t_stack = [t]
                while s_stack and t_stack:
                    s_node = s_stack.pop()
                    t_node = t_stack.pop()
                    if s_node.val != t_node.val:
                        break
                    else:
                        if bool(s_node.left) ^ bool(t_node.left):
                            break
                        elif t_node.left:
                            t_stack.append(t_node.left)
                            s_stack.append(s_node.left)

                        if bool(s_node.right) ^ bool(t_node.right):
                            break
                        elif t_node.right:
                            s_stack.append(s_node.right)
                            t_stack.append(t_node.right)
                    if len(s_stack) == len(t_stack) == 0:
                        return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
