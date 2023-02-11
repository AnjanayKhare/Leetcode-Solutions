
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n==0:
            return
        def merge(l, h):
            if l==h:
                print(l, h)
                return lists[l]
            mid = (l+h)//2
            l1 = merge(l, mid)
            l2 = merge(mid+1, h)
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l = ListNode(l1.val)
                l1 = l1.next
            else:
                l = ListNode(l2.val)
                l2 = l2.next
            root = l
            while l1 and l2:    
                if l1.val < l2.val:
                    temp = ListNode(l1.val)
                    l1 = l1.next
                else:
                    temp = ListNode(l2.val)
                    l2 = l2.next
                l.next = temp
                l = l.next
            if not l1:
                l.next = l2
            else:
                l.next = l1
            return root

        return merge(0, n-1)
