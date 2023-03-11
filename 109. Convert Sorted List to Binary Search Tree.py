# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return

        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        def make(l, h):
            if h<l:
                return
            
            mid = (l+h)>>1
            node = TreeNode(arr[mid])
            node.left = make(l, mid-1)
            node.right = make(mid+1, h)
            return node
        return make(0, len(arr)-1)
