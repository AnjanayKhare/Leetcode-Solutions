class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def trev(node, d):
            if node:
                if not d<len(ans):
                    ans.append([])
                ans[d].append(node.val)
                trev(node.left, d+1)
                trev(node.right, d+1)
        
        trev(root, 0)
        for i in range(1, len(ans), 2):
            ans[i] = ans[i][::-1]
        return ans
