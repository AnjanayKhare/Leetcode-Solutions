# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def bld(inord, preord):
            if not preord and not inord:
                return None
            root = TreeNode(preord[0])
            mid = inord.index(preord[0])
            root.left = bld(inord[:mid], preord[1:mid+1])
            root.right = bld(inord[mid+1:], preord[mid+1:])
            return root
        
        return bld(inorder, preorder)
