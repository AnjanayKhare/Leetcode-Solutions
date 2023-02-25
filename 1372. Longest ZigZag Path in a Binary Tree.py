class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def trev(node):
            if node:
                if not node.right:
                    node.rmx = 0
                else:
                    trev(node.right)
                    node.rmx = 1+node.right.lmx
                if not node.left:
                    node.lmx = 0
                else:
                    trev(node.left)
                    node.lmx = 1+node.left.rmx
                self.ans = max(self.ans, node.lmx, node.rmx)

        trev(root)
        
        return self.ans
