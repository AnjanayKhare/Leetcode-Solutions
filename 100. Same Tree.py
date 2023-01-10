class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def isSame(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1) ^ (not node2):
                return False
            return (node1.val == node2.val) and isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
        
        return isSame(p, q)
