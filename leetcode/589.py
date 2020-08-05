class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            res.append(root.val)
            for node in root.children:
                self.helper(node, res)
